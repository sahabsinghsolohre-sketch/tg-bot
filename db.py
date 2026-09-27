"""
Database storage for user balances, language, referrals, pending deposits, orders and stock accounts.
Supports both PostgreSQL (via Neon / DATABASE_URL env var) and local SQLite (bot.db fallback).
"""

import os
import random
import sqlite3
import threading
import time
from contextlib import contextmanager

DATABASE_URL = os.getenv("DATABASE_URL")
IS_POSTGRES = bool(DATABASE_URL)

if IS_POSTGRES:
    import psycopg2
    import psycopg2.extras

DB_PATH = "bot.db"

REFERRAL_PERCENT = 0.01
REFERRAL_MIN_DEPOSIT = 10.0

_lock = threading.Lock()

# A brand-new Postgres/Neon connection costs ~3 seconds; a query on a warm
# connection costs ~0.1 second. So one connection per thread is cached and reused
# instead of reconnecting on every single query.
IDLE_PING_AFTER = 45  # seconds of inactivity after which the cached conn is pinged
_local = threading.local()


def _raw_connect():
    """Open a brand-new database connection."""
    if IS_POSTGRES:
        return psycopg2.connect(
            DATABASE_URL, cursor_factory=psycopg2.extras.RealDictCursor
        )
    conn = sqlite3.connect(DB_PATH, timeout=30)
    conn.row_factory = sqlite3.Row
    return conn


def _drop_conn() -> None:
    """Forget (and close) the cached connection of the current thread."""
    conn = getattr(_local, "conn", None)
    _local.conn = None
    _local.used = 0.0
    if conn is not None:
        try:
            conn.close()
        except Exception:
            pass


def _connection():
    """Return this thread's reusable connection, reconnecting only when stale."""
    conn = getattr(_local, "conn", None)
    if conn is not None:
        if time.time() - getattr(_local, "used", 0.0) < IDLE_PING_AFTER:
            return conn
        try:
            cur = conn.cursor()
            cur.execute("SELECT 1")  # cheap keep-alive check after an idle period
            cur.close()
            return conn
        except Exception:
            _drop_conn()
    conn = _raw_connect()
    _local.conn = conn
    _local.used = time.time()
    return conn


@contextmanager
def _connect():
    conn = _connection()
    try:
        yield conn
        # A read-only block needs no COMMIT round trip — that alone halves the
        # latency of every "open the shop / my orders" press on a remote database.
        if not IS_POSTGRES or getattr(_local, "dirty", False):
            conn.commit()
        _local.dirty = False
    except Exception:
        try:
            conn.rollback()
        except Exception:
            _drop_conn()
        _local.dirty = False
        raise
    finally:
        _local.used = time.time()


def _is_write(sql: str) -> bool:
    """True when a statement changes data (so a COMMIT round trip is needed)."""
    head = sql.lstrip().split(None, 1)
    return bool(head) and head[0].lower() in (
        "insert",
        "update",
        "delete",
        "alter",
        "create",
        "drop",
        "truncate",
        "replace",
        "with",
    )


def _mark_dirty() -> None:
    """Force the next ``_connect()`` exit to commit (used by raw-cursor writes)."""
    _local.dirty = True


# --- tiny in-process caches --------------------------------------------------
# A round trip to the hosted Postgres takes ~0.5-1s, so short-lived snapshots keep
# button presses snappy while still showing freshly decayed / updated values.
STOCK_CACHE_TTL = 15   # seconds a stock snapshot may be reused
LANG_CACHE_TTL = 300   # seconds a cached user language may be reused
PRODUCT_CACHE_TTL = 30  # seconds a cached catalog listing may be reused

_cache: dict = {}
_cache_lock = threading.Lock()


def _cache_get(key, ttl: float):
    with _cache_lock:
        hit = _cache.get(key)
    if hit is None:
        return None
    stored_at, value = hit
    if time.time() - stored_at > ttl:
        return None
    return value


def _cache_set(key, value) -> None:
    with _cache_lock:
        _cache[key] = (time.time(), value)


def _cache_invalidate(*keys) -> None:
    with _cache_lock:
        for key in keys:
            _cache.pop(key, None)


def clear_caches() -> None:
    """Drop every cached snapshot (called after stock or catalog changes)."""
    with _cache_lock:
        _cache.clear()


def _exec(conn, sql: str, params: tuple = ()):
    """Execute SQL query with driver-appropriate parameter placeholder replacement."""
    if _is_write(sql):
        _mark_dirty()
    if IS_POSTGRES:
        pg_sql = sql.replace("?", "%s")
        if "ROUND(unique_amount, 4)" in pg_sql:
            pg_sql = pg_sql.replace("ROUND(unique_amount, 4)", "ROUND(CAST(unique_amount AS numeric), 4)")
        if "ROUND(%s, 4)" in pg_sql:
            pg_sql = pg_sql.replace("ROUND(%s, 4)", "ROUND(CAST(%s AS numeric), 4)")
        cur = conn.cursor()
        cur.execute(pg_sql, params)
        return cur
    else:
        return conn.execute(sql, params)


def _column_exists(conn, table: str, column: str) -> bool:
    if IS_POSTGRES:
        cur = conn.cursor()
        cur.execute(
            "SELECT 1 FROM information_schema.columns WHERE table_name = %s AND column_name = %s",
            (table, column),
        )
        return cur.fetchone() is not None
    else:
        rows = conn.execute(f"PRAGMA table_info({table})").fetchall()
        return any(r["name"] == column for r in rows)


def init_db() -> None:
    """Create tables if they don't exist, and add any missing columns (migrations)."""
    with _lock, _connect() as conn:
        if IS_POSTGRES:
            _mark_dirty()  # raw-cursor DDL below must be committed
            cur = conn.cursor()
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    user_id           BIGINT PRIMARY KEY,
                    balance           DOUBLE PRECISION NOT NULL DEFAULT 0,
                    orders            INTEGER NOT NULL DEFAULT 0,
                    language          TEXT NOT NULL DEFAULT 'en',
                    referred_by       BIGINT,
                    referrals          INTEGER NOT NULL DEFAULT 0,
                    referral_earnings  DOUBLE PRECISION NOT NULL DEFAULT 0,
                    deposits_count     INTEGER NOT NULL DEFAULT 0,
                    referral_qualified INTEGER NOT NULL DEFAULT 0
                );

                CREATE TABLE IF NOT EXISTS pending_deposits (
                    id            SERIAL PRIMARY KEY,
                    user_id       BIGINT NOT NULL,
                    base_amount   DOUBLE PRECISION NOT NULL,
                    unique_amount DOUBLE PRECISION NOT NULL,
                    created_at    BIGINT NOT NULL,
                    expires_at    BIGINT NOT NULL,
                    status        TEXT NOT NULL DEFAULT 'pending',
                    tx_hash       TEXT
                );

                CREATE INDEX IF NOT EXISTS idx_pending_status
                    ON pending_deposits(status);

                CREATE TABLE IF NOT EXISTS orders (
                    id           SERIAL PRIMARY KEY,
                    user_id      BIGINT NOT NULL,
                    product_id   TEXT NOT NULL,
                    product_name TEXT NOT NULL,
                    price        DOUBLE PRECISION NOT NULL,
                    created_at   BIGINT NOT NULL
                );

                CREATE INDEX IF NOT EXISTS idx_orders_user
                    ON orders(user_id);

                CREATE TABLE IF NOT EXISTS products (
                    id          TEXT PRIMARY KEY,
                    name        TEXT NOT NULL,
                    price       DOUBLE PRECISION NOT NULL,
                    description TEXT NOT NULL,
                    stock       INTEGER,
                    delivery    TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS product_stock (
                    product_id TEXT PRIMARY KEY,
                    stock      INTEGER
                );

                CREATE TABLE IF NOT EXISTS product_accounts (
                    id            SERIAL PRIMARY KEY,
                    product_id    TEXT NOT NULL,
                    account_data  TEXT NOT NULL,
                    is_sold       INTEGER NOT NULL DEFAULT 0,
                    created_at    BIGINT NOT NULL
                );

                CREATE INDEX IF NOT EXISTS idx_accounts_prod_sold
                    ON product_accounts(product_id, is_sold);
                """
            )
        else:
            conn.executescript(
                """
                CREATE TABLE IF NOT EXISTS users (
                    user_id           INTEGER PRIMARY KEY,
                    balance           REAL NOT NULL DEFAULT 0,
                    orders            INTEGER NOT NULL DEFAULT 0,
                    language          TEXT NOT NULL DEFAULT 'en',
                    referred_by       INTEGER,
                    referrals          INTEGER NOT NULL DEFAULT 0,
                    referral_earnings  REAL NOT NULL DEFAULT 0,
                    deposits_count     INTEGER NOT NULL DEFAULT 0,
                    referral_qualified INTEGER NOT NULL DEFAULT 0
                );

                CREATE TABLE IF NOT EXISTS pending_deposits (
                    id            INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id       INTEGER NOT NULL,
                    base_amount   REAL NOT NULL,
                    unique_amount REAL NOT NULL,
                    created_at    INTEGER NOT NULL,
                    expires_at    INTEGER NOT NULL,
                    status        TEXT NOT NULL DEFAULT 'pending',
                    tx_hash       TEXT
                );

                CREATE INDEX IF NOT EXISTS idx_pending_status
                    ON pending_deposits(status);

                CREATE TABLE IF NOT EXISTS orders (
                    id           SERIAL PRIMARY KEY,
                    user_id      INTEGER NOT NULL,
                    product_id   TEXT NOT NULL,
                    product_name TEXT NOT NULL,
                    price        REAL NOT NULL,
                    created_at   INTEGER NOT NULL
                );

                CREATE INDEX IF NOT EXISTS idx_orders_user
                    ON orders(user_id);

                CREATE TABLE IF NOT EXISTS products (
                    id          TEXT PRIMARY KEY,
                    name        TEXT NOT NULL,
                    price       REAL NOT NULL,
                    description TEXT NOT NULL,
                    stock       INTEGER,  -- NULL means unlimited
                    delivery    TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS product_stock (
                    product_id TEXT PRIMARY KEY,
                    stock      INTEGER   -- NULL means unlimited
                );

                CREATE TABLE IF NOT EXISTS product_accounts (
                    id            INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_id    TEXT NOT NULL,
                    account_data  TEXT NOT NULL,
                    is_sold       INTEGER NOT NULL DEFAULT 0,
                    created_at    INTEGER NOT NULL
                );

                CREATE INDEX IF NOT EXISTS idx_accounts_prod_sold
                    ON product_accounts(product_id, is_sold);
                """
            )

        for col, ddl in [
            ("language", "ALTER TABLE users ADD COLUMN language TEXT NOT NULL DEFAULT 'en'"),
            ("referred_by", "ALTER TABLE users ADD COLUMN referred_by BIGINT" if IS_POSTGRES else "ALTER TABLE users ADD COLUMN referred_by INTEGER"),
            ("referrals", "ALTER TABLE users ADD COLUMN referrals INTEGER NOT NULL DEFAULT 0"),
            ("referral_earnings", "ALTER TABLE users ADD COLUMN referral_earnings DOUBLE PRECISION NOT NULL DEFAULT 0" if IS_POSTGRES else "ALTER TABLE users ADD COLUMN referral_earnings REAL NOT NULL DEFAULT 0"),
            ("deposits_count", "ALTER TABLE users ADD COLUMN deposits_count INTEGER NOT NULL DEFAULT 0"),
            ("referral_qualified", "ALTER TABLE users ADD COLUMN referral_qualified INTEGER NOT NULL DEFAULT 0"),
        ]:
            if not _column_exists(conn, "users", col):
                _exec(conn, ddl)


def ensure_user(user_id: int) -> None:
    """Create a user row if it doesn't exist yet."""
    with _lock, _connect() as conn:
        _exec(
            conn,
            "INSERT INTO users (user_id) VALUES (?) ON CONFLICT (user_id) DO NOTHING",
            (user_id,),
        )


def get_language(user_id: int) -> str:
    cached = _cache_get(("lang", user_id), LANG_CACHE_TTL)
    if cached is not None:
        return cached
    with _connect() as conn:
        cur = _exec(
            conn,
            "SELECT language FROM users WHERE user_id = ?",
            (user_id,),
        )
        row = cur.fetchone()
    lang = row["language"] if row else "en"
    _cache_set(("lang", user_id), lang)
    return lang


def touch_user(user_id: int) -> str:
    """Create the user row if missing and return their language.

    The write only happens the first time a user is seen in this process — after
    that the cached language is used, so an ordinary button press costs zero
    database round trips just for identifying the user.
    """
    cached = _cache_get(("lang", user_id), LANG_CACHE_TTL)
    if cached is not None:
        return cached

    with _lock, _connect() as conn:
        if IS_POSTGRES:
            cur = _exec(
                conn,
                "INSERT INTO users (user_id) VALUES (?) "
                "ON CONFLICT (user_id) DO UPDATE SET user_id = EXCLUDED.user_id "
                "RETURNING language",
                (user_id,),
            )
        else:
            cur = _exec(
                conn,
                "INSERT INTO users (user_id) VALUES (?) "
                "ON CONFLICT (user_id) DO UPDATE SET language = users.language "
                "RETURNING language",
                (user_id,),
            )
        row = cur.fetchone()
    lang = row["language"] if row else "en"
    _cache_set(("lang", user_id), lang)
    return lang


def set_language(user_id: int, language: str) -> None:
    with _lock, _connect() as conn:
        _exec(
            conn,
            """
            INSERT INTO users (user_id, language) VALUES (?, ?)
            ON CONFLICT(user_id) DO UPDATE SET language = EXCLUDED.language
            """,
            (user_id, language),
        )
    _cache_set(("lang", user_id), language)


def get_balance(user_id: int) -> float:
    with _connect() as conn:
        cur = _exec(
            conn,
            "SELECT balance FROM users WHERE user_id = ?",
            (user_id,),
        )
        row = cur.fetchone()
        return float(row["balance"]) if row else 0.0


def get_user(user_id: int) -> dict:
    """Return full profile info for a user (defaults if new)."""
    with _connect() as conn:
        cur = _exec(
            conn,
            "SELECT balance, orders, language, referred_by, referrals, "
            "referral_earnings, deposits_count FROM users WHERE user_id = ?",
            (user_id,),
        )
        row = cur.fetchone()
        if row:
            return {
                "balance": float(row["balance"]),
                "orders": int(row["orders"]),
                "language": row["language"],
                "referred_by": row["referred_by"],
                "referrals": int(row["referrals"]),
                "referral_earnings": float(row["referral_earnings"]),
                "deposits_count": int(row["deposits_count"]),
            }
        return {
            "balance": 0.0,
            "orders": 0,
            "language": "en",
            "referred_by": None,
            "referrals": 0,
            "referral_earnings": 0.0,
            "deposits_count": 0,
        }


def credit_balance(user_id: int, amount: float) -> float:
    """Add `amount` to a user's balance, creating the row if needed. Returns new balance."""
    with _lock, _connect() as conn:
        _exec(
            conn,
            """
            INSERT INTO users (user_id, balance) VALUES (?, ?)
            ON CONFLICT(user_id) DO UPDATE SET balance = users.balance + EXCLUDED.balance
            """,
            (user_id, amount),
        )
        cur = _exec(
            conn,
            "SELECT balance FROM users WHERE user_id = ?",
            (user_id,),
        )
        row = cur.fetchone()
        return float(row["balance"])


def set_referrer(user_id: int, referrer_id: int) -> bool:
    if user_id == referrer_id:
        return False
    with _lock, _connect() as conn:
        _exec(conn, "INSERT INTO users (user_id) VALUES (?) ON CONFLICT (user_id) DO NOTHING", (user_id,))
        cur = _exec(conn, "SELECT referred_by FROM users WHERE user_id = ?", (user_id,))
        row = cur.fetchone()
        if row and row["referred_by"] is not None:
            return False  # already referred by someone
        _exec(conn, "INSERT INTO users (user_id) VALUES (?) ON CONFLICT (user_id) DO NOTHING", (referrer_id,))
        _exec(
            conn,
            "UPDATE users SET referred_by = ? WHERE user_id = ?",
            (referrer_id, user_id),
        )
        return True


def reward_referrer_for_deposit(depositor_id: int, deposit_amount: float) -> dict | None:
    with _lock, _connect() as conn:
        _exec(conn, "INSERT INTO users (user_id) VALUES (?) ON CONFLICT (user_id) DO NOTHING", (depositor_id,))
        cur = _exec(
            conn,
            "SELECT referred_by, referral_qualified FROM users WHERE user_id = ?",
            (depositor_id,),
        )
        row = cur.fetchone()
        already_qualified = int(row["referral_qualified"]) if row else 0
        referrer_id = row["referred_by"] if row else None

        _exec(
            conn,
            "UPDATE users SET deposits_count = deposits_count + 1 WHERE user_id = ?",
            (depositor_id,),
        )

        if referrer_id is None or deposit_amount < REFERRAL_MIN_DEPOSIT:
            return None

        reward = round(deposit_amount * REFERRAL_PERCENT, 2)
        if reward <= 0:
            return None

        if not already_qualified:
            _exec(
                conn,
                "UPDATE users SET referral_qualified = 1 WHERE user_id = ?",
                (depositor_id,),
            )
            _exec(
                conn,
                "UPDATE users SET referrals = referrals + 1, "
                "referral_earnings = referral_earnings + ?, "
                "balance = balance + ? WHERE user_id = ?",
                (reward, reward, referrer_id),
            )
        else:
            _exec(
                conn,
                "UPDATE users SET referral_earnings = referral_earnings + ?, "
                "balance = balance + ? WHERE user_id = ?",
                (reward, reward, referrer_id),
            )

        cur_bal = _exec(
            conn,
            "SELECT balance FROM users WHERE user_id = ?",
            (referrer_id,),
        )
        new_bal = cur_bal.fetchone()
        return {
            "referrer_id": referrer_id,
            "reward": reward,
            "new_referrer_balance": float(new_bal["balance"]) if new_bal else 0.0,
        }


def has_open_deposit(user_id: int) -> bool:
    with _connect() as conn:
        cur = _exec(
            conn,
            "SELECT 1 FROM pending_deposits WHERE user_id = ? AND status = 'pending'",
            (user_id,),
        )
        return cur.fetchone() is not None


def unique_amount_taken(unique_amount: float) -> bool:
    """True if another pending deposit already uses this exact amount."""
    with _connect() as conn:
        cur = _exec(
            conn,
            "SELECT 1 FROM pending_deposits "
            "WHERE status = 'pending' AND ROUND(unique_amount, 4) = ROUND(?, 4)",
            (unique_amount,),
        )
        return cur.fetchone() is not None


def create_pending_deposit(
    user_id: int, base_amount: float, unique_amount: float, window_minutes: int
) -> dict:
    now = int(time.time())
    expires = now + window_minutes * 60
    with _lock, _connect() as conn:
        if IS_POSTGRES:
            cur = _exec(
                conn,
                """
                INSERT INTO pending_deposits
                    (user_id, base_amount, unique_amount, created_at, expires_at, status)
                VALUES (?, ?, ?, ?, ?, 'pending')
                RETURNING id
                """,
                (user_id, base_amount, unique_amount, now, expires),
            )
            inserted_id = cur.fetchone()["id"]
        else:
            cur = _exec(
                conn,
                """
                INSERT INTO pending_deposits
                    (user_id, base_amount, unique_amount, created_at, expires_at, status)
                VALUES (?, ?, ?, ?, ?, 'pending')
                """,
                (user_id, base_amount, unique_amount, now, expires),
            )
            inserted_id = cur.lastrowid

        return {
            "id": inserted_id,
            "user_id": user_id,
            "base_amount": base_amount,
            "unique_amount": unique_amount,
            "expires_at": expires,
        }


def get_open_deposits() -> list:
    with _connect() as conn:
        cur = _exec(
            conn,
            "SELECT * FROM pending_deposits WHERE status = 'pending'",
        )
        rows = cur.fetchall()
        return [dict(r) for r in rows]


def mark_paid(deposit_id: int, tx_hash: str) -> None:
    with _lock, _connect() as conn:
        _exec(
            conn,
            "UPDATE pending_deposits SET status = 'paid', tx_hash = ? WHERE id = ?",
            (tx_hash, deposit_id),
        )


def expire_old_deposits() -> None:
    now = int(time.time())
    with _lock, _connect() as conn:
        _exec(
            conn,
            "UPDATE pending_deposits SET status = 'expired' "
            "WHERE status = 'pending' AND expires_at < ?",
            (now,),
        )


# --- Account Inventory Stock System -----------------------------------------
def add_accounts_to_stock(product_id: str, accounts: list[str]) -> int:
    """
    Add account credential lines (e.g. ['email1:pass1', 'email2:pass2']) to product_accounts inventory.
    Returns count of added accounts.
    """
    if not accounts:
        return 0
    now = int(time.time())
    count = 0
    with _lock, _connect() as conn:
        for acc in accounts:
            acc = acc.strip()
            if acc:
                _exec(
                    conn,
                    "INSERT INTO product_accounts (product_id, account_data, is_sold, created_at) VALUES (?, ?, 0, ?)",
                    (product_id, acc, now),
                )
                count += 1

        # Sync stock count
        s_cur = _exec(
            conn,
            "SELECT COUNT(*) AS c FROM product_accounts WHERE product_id = ? AND is_sold = 0",
            (product_id,),
        )
        s_row = s_cur.fetchone()
        new_stock = int(s_row["c"]) if s_row else 0

        _exec(
            conn,
            "UPDATE products SET stock = ? WHERE id = ?",
            (new_stock, product_id),
        )
        _exec(
            conn,
            """
            INSERT INTO product_stock (product_id, stock) VALUES (?, ?)
            ON CONFLICT(product_id) DO UPDATE SET stock = EXCLUDED.stock
            """,
            (product_id, new_stock),
        )
    _cache_invalidate("stock_maps")
    return count


# --- Product catalog & stock --------------------------------------------------
STOCK_CAP = 100  # a product may never be seeded with 100 or more


def _clean_seed_stock(value, fallback: int = 1):
    """Normalise the stock value used when a product is first inserted.

    ``None`` stays ``None`` (= unlimited). Anything <= 0 or >= 100 is replaced by
    a random value below 100 so the shop never shows a flat "100" or a 0 that was
    not caused by real sales.
    """
    if value is None:
        return None
    try:
        value = int(value)
    except (TypeError, ValueError):
        return fallback
    if value <= 0 or value >= STOCK_CAP:
        return random.randint(1, 99)
    return value


def seed_products(products: list) -> None:
    """
    UPSERT of the catalog — inserts new products and updates existing ones
    including setting stock to Unlimited (NULL).
    """
    with _lock, _connect() as conn:
        for p in products:
            pid = p["id"]
            name = p["name"]
            price = float(p["price"])
            desc = p["description"]
            stock = p.get("stock")  # None for Unlimited
            delivery = p.get("delivery", "")

            if IS_POSTGRES:
                _exec(
                    conn,
                    """
                    INSERT INTO products (id, name, price, description, stock, delivery)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON CONFLICT (id) DO UPDATE SET
                        name        = EXCLUDED.name,
                        price       = EXCLUDED.price,
                        description = EXCLUDED.description,
                        stock       = EXCLUDED.stock,
                        delivery    = EXCLUDED.delivery
                    """,
                    (pid, name, price, desc, stock, delivery),
                )
                _exec(
                    conn,
                    """
                    INSERT INTO product_stock (product_id, stock)
                    VALUES (%s, %s)
                    ON CONFLICT (product_id) DO UPDATE SET stock = EXCLUDED.stock
                    """,
                    (pid, stock),
                )
            else:
                _exec(
                    conn,
                    """
                    INSERT INTO products (id, name, price, description, stock, delivery)
                    VALUES (?, ?, ?, ?, ?, ?)
                    ON CONFLICT(id) DO UPDATE SET
                        name        = excluded.name,
                        price       = excluded.price,
                        description = excluded.description,
                        stock       = excluded.stock,
                        delivery    = excluded.delivery
                    """,
                    (pid, name, price, desc, stock, delivery),
                )
                _exec(
                    conn,
                    """
                    INSERT INTO product_stock (product_id, stock)
                    VALUES (?, ?)
                    ON CONFLICT (product_id) DO UPDATE SET stock = excluded.stock
                    """,
                    (pid, stock),
                )
    clear_caches()  # catalog/stock snapshots are stale after a re-seed


def get_all_products() -> list:
    """Every product row, cached for :data:`PRODUCT_CACHE_TTL` seconds.

    The catalog only changes through the admin commands (which clear the cache),
    so a cached copy removes a remote round trip from every shop/detail view.
    Returned dicts are copies — callers may freely mutate them.
    """
    cached = _cache_get("products", PRODUCT_CACHE_TTL)
    if cached is None:
        with _connect() as conn:
            cur = _exec(
                conn,
                "SELECT id, name, price, description, stock, delivery FROM products",
            )
            rows = cur.fetchall()
        cached = [dict(r) for r in rows]
        _cache_set("products", cached)
    return [dict(p) for p in cached]


def get_product(product_id: str) -> dict | None:
    for p in get_all_products():
        if p["id"] == product_id:
            return p
    return None


def add_product(
    product_id: str,
    name: str,
    price: float,
    description: str,
    stock: int | None = 0,
    delivery: str = "",
) -> None:
    with _lock, _connect() as conn:
        cur = _exec(
            conn,
            "UPDATE products SET name = ?, price = ?, description = ?, stock = ?, delivery = ? WHERE id = ?",
            (name, price, description, stock, delivery, product_id),
        )
        if cur.rowcount == 0:
            _exec(
                conn,
                "INSERT INTO products (id, name, price, description, stock, delivery) VALUES (?, ?, ?, ?, ?, ?)",
                (product_id, name, price, description, stock, delivery),
            )
        _exec(
            conn,
            "INSERT INTO product_stock (product_id, stock) VALUES (?, ?) ON CONFLICT (product_id) DO UPDATE SET stock = EXCLUDED.stock" if IS_POSTGRES else "INSERT INTO product_stock (product_id, stock) VALUES (?, ?) ON CONFLICT (product_id) DO UPDATE SET stock = excluded.stock",
            (product_id, stock),
        )
    clear_caches()


def delete_product(product_id: str) -> bool:
    """
    Remove a product from the catalog (products + product_stock tables).
    Returns True if a row was actually deleted, False if not found.
    """
    with _lock, _connect() as conn:
        cur = _exec(conn, "DELETE FROM products WHERE id = ?", (product_id,))
        deleted = cur.rowcount > 0
        _exec(conn, "DELETE FROM product_stock WHERE product_id = ?", (product_id,))
    clear_caches()
    return deleted


def seed_stock(products: list) -> None:
    with _lock, _connect() as conn:
        for p in products:
            _exec(
                conn,
                "INSERT INTO product_stock (product_id, stock) VALUES (?, ?) ON CONFLICT (product_id) DO NOTHING",
                (p["id"], p.get("stock")),
            )


def get_stock(product_id: str):
    """Current stock of one product (``None`` = unlimited).

    Reads the cached stock snapshot, so opening a product page costs no extra
    database round trip at all.
    """
    return get_stocks([product_id]).get(product_id)


_STOCK_SNAPSHOT_SQL = """
SELECT 'acc' AS src, product_id AS pid, COUNT(*) AS c,
       SUM(CASE WHEN is_sold = 0 THEN 1 ELSE 0 END) AS u
  FROM product_accounts GROUP BY product_id
UNION ALL
SELECT 'stock', product_id, stock, NULL FROM product_stock
UNION ALL
SELECT 'prod', id, stock, NULL FROM products
"""


def _stock_maps(refresh: bool = False):
    """Return (accounts, unsold, stocks, products) maps using ONE query, cached briefly."""
    if not refresh:
        cached = _cache_get("stock_maps", STOCK_CACHE_TTL)
        if cached is not None:
            return cached

    with _connect() as conn:
        rows = _exec(conn, _STOCK_SNAPSHOT_SQL).fetchall()

    accounts, unsold, stocks, products = {}, {}, {}, {}
    for row in rows:
        src = row["src"]
        pid = row["pid"]
        if src == "acc":
            accounts[pid] = int(row["c"] or 0)
            unsold[pid] = int(row["u"] or 0)
        elif row["c"] is not None:
            (stocks if src == "stock" else products)[pid] = row["c"]

    maps = (accounts, unsold, stocks, products)
    _cache_set("stock_maps", maps)
    return maps


def inventory_products() -> set:
    """Ids of products whose stock is a real account-inventory count.

    Those numbers must never be faked by the background stock jobs.
    """
    accounts, _unsold, _stocks, _products = _stock_maps()
    return set(accounts)


def get_stocks(product_ids: list[str] | None = None, refresh: bool = False) -> dict:
    """Return ``{product_id: stock}`` for many products in a single query.

    Uses the same priority as :func:`get_stock`: unsold account inventory first,
    then the ``product_stock`` table, then the ``products`` table. ``None`` means
    unlimited. The snapshot is cached for :data:`STOCK_CACHE_TTL` seconds so a
    button press does not wait for a fresh remote round trip every time; pass
    ``refresh=True`` to force a re-read (used by the background cache warmer).
    """
    accounts, unsold, stocks, products = _stock_maps(refresh=refresh)

    ids = (
        list(product_ids)
        if product_ids is not None
        else sorted(set(stocks) | set(products))
    )
    result = {}
    for pid in ids:
        if accounts.get(pid, 0) > 0:
            result[pid] = unsold.get(pid, 0)
        elif stocks.get(pid) is not None:
            result[pid] = stocks[pid]
        else:
            result[pid] = products.get(pid)
    return result


def set_stocks(values: dict) -> int:
    """Update the stock of many products in as few round trips as possible.

    Used by the background stock jobs so they never flood the database with one
    connection (or one query) per product.
    """
    if not values:
        return 0
    items = [(pid, stock) for pid, stock in values.items()]
    with _lock, _connect() as conn:
        _mark_dirty()
        if IS_POSTGRES:
            with conn.cursor() as cur:
                psycopg2.extras.execute_values(
                    cur,
                    "INSERT INTO product_stock (product_id, stock) VALUES %s "
                    "ON CONFLICT (product_id) DO UPDATE SET stock = EXCLUDED.stock",
                    items,
                )
            with conn.cursor() as cur:
                psycopg2.extras.execute_values(
                    cur,
                    "UPDATE products AS p SET stock = v.stock "
                    "FROM (VALUES %s) AS v(id, stock) WHERE p.id = v.id",
                    items,
                )
        else:
            conn.executemany(
                "INSERT INTO product_stock (product_id, stock) VALUES (?, ?) "
                "ON CONFLICT(product_id) DO UPDATE SET stock = EXCLUDED.stock",
                items,
            )
            conn.executemany(
                "UPDATE products SET stock = ? WHERE id = ?",
                [(stock, pid) for pid, stock in items],
            )
    _cache_invalidate("stock_maps")
    return len(items)


def set_stock(product_id: str, new_stock: int | None) -> bool:
    with _lock, _connect() as conn:
        p_row = _exec(conn, "SELECT 1 FROM products WHERE id = ?", (product_id,)).fetchone()
        s_row = _exec(conn, "SELECT 1 FROM product_stock WHERE product_id = ?", (product_id,)).fetchone()

        if not p_row and not s_row:
            return False

        if p_row:
            _exec(
                conn,
                "UPDATE products SET stock = ? WHERE id = ?",
                (new_stock, product_id),
            )
        _exec(
            conn,
            """
            INSERT INTO product_stock (product_id, stock) VALUES (?, ?)
            ON CONFLICT(product_id) DO UPDATE SET stock = EXCLUDED.stock
            """,
            (product_id, new_stock),
        )
        _cache_invalidate("stock_maps")
        return True


def adjust_stock(product_id: str, delta: int) -> tuple[bool, int | None]:
    with _lock, _connect() as conn:
        row = _exec(conn, "SELECT stock FROM product_stock WHERE product_id = ?", (product_id,)).fetchone()

        if not row:
            p_row = _exec(conn, "SELECT stock FROM products WHERE id = ?", (product_id,)).fetchone()
            if not p_row:
                return False, None
            current_stock = p_row["stock"]
        else:
            current_stock = row["stock"]

        if current_stock is None:
            if delta >= 0:
                new_stock = delta
            else:
                return False, None
        else:
            new_stock = max(0, current_stock + delta)

        _exec(
            conn,
            "UPDATE products SET stock = ? WHERE id = ?",
            (new_stock, product_id),
        )
        _exec(
            conn,
            """
            INSERT INTO product_stock (product_id, stock) VALUES (?, ?)
            ON CONFLICT(product_id) DO UPDATE SET stock = EXCLUDED.stock
            """,
            (product_id, new_stock),
        )
        _cache_invalidate("stock_maps")
        return True, new_stock


# --- Purchases / orders -----------------------------------------------------
_PURCHASE_INFO_SQL = """
SELECT
    (SELECT a.id FROM product_accounts a
      WHERE a.product_id = ? AND a.is_sold = 0 ORDER BY a.id ASC LIMIT 1) AS acc_id,
    (SELECT a.account_data FROM product_accounts a
      WHERE a.product_id = ? AND a.is_sold = 0 ORDER BY a.id ASC LIMIT 1) AS acc_data,
    (SELECT COUNT(*) FROM product_accounts a
      WHERE a.product_id = ?)                                             AS acc_total,
    (SELECT COUNT(*) FROM product_accounts a
      WHERE a.product_id = ? AND a.is_sold = 0)                           AS acc_unsold,
    (SELECT s.stock FROM product_stock s WHERE s.product_id = ?)          AS stock_row,
    (SELECT p.stock FROM products p WHERE p.id = ?)                       AS stock_prod,
    (SELECT u.balance FROM users u WHERE u.user_id = ?)                   AS balance
"""


def purchase(user_id: int, product: dict) -> dict:
    """Sell one unit of ``product`` to ``user_id`` (stock, balance and order row).

    The whole flow is kept to a handful of statements so a purchase on a remote
    database stays fast — every extra statement costs a full round trip.
    """
    price = float(product["price"])
    pid = product["id"]
    now = int(time.time())

    with _lock, _connect() as conn:
        _exec(
            conn,
            "INSERT INTO users (user_id) VALUES (?) ON CONFLICT (user_id) DO NOTHING",
            (user_id,),
        )

        # One query for pending account + stock + balance.
        info = _exec(
            conn,
            _PURCHASE_INFO_SQL,
            (pid, pid, pid, pid, pid, pid, user_id),
        ).fetchone()

        acc_id = info["acc_id"] if info else None
        acc_total = int(info["acc_total"] or 0) if info else 0
        acc_unsold = int(info["acc_unsold"] or 0) if info else 0
        stock_row = info["stock_row"] if info else None
        stock_prod = info["stock_prod"] if info else None
        balance = float(info["balance"] or 0) if info else 0.0

        # Same priority as get_stock(): account inventory wins over plain stock.
        if acc_total > 0:
            stock = acc_unsold
        elif stock_row is not None:
            stock = stock_row
        else:
            stock = stock_prod

        if stock is not None and stock <= 0:
            return {"ok": False, "reason": "out_of_stock"}

        if balance < price:
            return {
                "ok": False,
                "reason": "insufficient",
                "balance": balance,
                "price": price,
            }

        delivery_text = (
            info["acc_data"] if acc_id is not None else (product.get("delivery") or "Digital Item")
        )

        # Deduct balance + count the order in one statement.
        _exec(
            conn,
            "UPDATE users SET balance = balance - ?, orders = orders + 1 WHERE user_id = ?",
            (price, user_id),
        )

        if acc_id is not None:
            _exec(
                conn,
                "UPDATE product_accounts SET is_sold = 1 WHERE id = ?",
                (acc_id,),
            )
            # One row was sold, so the synced stock count is simply unsold - 1
            # (no extra COUNT round trip needed).
            remaining = max(0, acc_unsold - 1)
            _exec(
                conn,
                "UPDATE products SET stock = ? WHERE id = ?",
                (remaining, pid),
            )
            _exec(
                conn,
                "INSERT INTO product_stock (product_id, stock) VALUES (?, ?) "
                "ON CONFLICT(product_id) DO UPDATE SET stock = EXCLUDED.stock",
                (pid, remaining),
            )
        elif stock is not None:
            _exec(
                conn,
                "UPDATE product_stock SET stock = stock - 1 WHERE product_id = ?",
                (pid,),
            )
            _exec(conn, "UPDATE products SET stock = stock - 1 WHERE id = ?", (pid,))

        if IS_POSTGRES:
            cur = _exec(
                conn,
                "INSERT INTO orders (user_id, product_id, product_name, price, created_at) "
                "VALUES (?, ?, ?, ?, ?) RETURNING id",
                (user_id, pid, product["name"], price, now),
            )
            order_id = cur.fetchone()["id"]
        else:
            cur = _exec(
                conn,
                "INSERT INTO orders (user_id, product_id, product_name, price, created_at) "
                "VALUES (?, ?, ?, ?, ?)",
                (user_id, pid, product["name"], price, now),
            )
            order_id = cur.lastrowid

    _cache_invalidate("stock_maps")
    return {
        "ok": True,
        "order_id": order_id,
        "new_balance": balance - price,
        "delivery": delivery_text,
    }


def get_orders(user_id: int, limit: int = 10) -> list:
    with _connect() as conn:
        cur = _exec(
            conn,
            "SELECT id, product_name, price, created_at FROM orders "
            "WHERE user_id = ? ORDER BY id DESC LIMIT ?",
            (user_id, limit),
        )
        rows = cur.fetchall()
        return [dict(r) for r in rows]


def count_orders(user_id: int) -> int:
    with _connect() as conn:
        cur = _exec(
            conn,
            "SELECT COUNT(*) AS c FROM orders WHERE user_id = ?",
            (user_id,),
        )
        row = cur.fetchone()
        return int(row["c"]) if row else 0
