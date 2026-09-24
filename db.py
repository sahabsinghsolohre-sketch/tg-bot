"""
Database storage for user balances, language, referrals, pending deposits, orders and stock accounts.
Supports both PostgreSQL (via Neon / DATABASE_URL env var) and local SQLite (bot.db fallback).
"""

import os
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


@contextmanager
def _connect():
    if IS_POSTGRES:
        conn = psycopg2.connect(DATABASE_URL, cursor_factory=psycopg2.extras.RealDictCursor)
        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()
    else:
        conn = sqlite3.connect(DB_PATH, timeout=30)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            conn.commit()
        finally:
            conn.close()


def _exec(conn, sql: str, params: tuple = ()):
    """Execute SQL query with driver-appropriate parameter placeholder replacement."""
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
    with _connect() as conn:
        cur = _exec(
            conn,
            "SELECT language FROM users WHERE user_id = ?",
            (user_id,),
        )
        row = cur.fetchone()
        return row["language"] if row else "en"


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
    return count


# --- Product catalog & stock --------------------------------------------------
def seed_products(products: list) -> None:
    with _lock, _connect() as conn:
        for p in products:
            cur = _exec(
                conn,
                "UPDATE products SET name = ?, price = ?, description = ?, delivery = ? WHERE id = ?",
                (p["name"], float(p["price"]), p["description"], p.get("delivery", ""), p["id"]),
            )
            if cur.rowcount == 0:
                _exec(
                    conn,
                    "INSERT INTO products (id, name, price, description, stock, delivery) VALUES (?, ?, ?, ?, ?, ?)",
                    (p["id"], p["name"], float(p["price"]), p["description"], p.get("stock", 0), p.get("delivery", "")),
                )
            _exec(
                conn,
                "INSERT INTO product_stock (product_id, stock) VALUES (?, ?) ON CONFLICT (product_id) DO NOTHING",
                (p["id"], p.get("stock", 0)),
            )


def get_all_products() -> list:
    with _connect() as conn:
        cur = _exec(
            conn,
            "SELECT id, name, price, description, stock, delivery FROM products",
        )
        rows = cur.fetchall()
        return [dict(r) for r in rows]


def get_product(product_id: str) -> dict | None:
    with _connect() as conn:
        cur = _exec(
            conn,
            "SELECT id, name, price, description, stock, delivery FROM products WHERE id = ?",
            (product_id,),
        )
        row = cur.fetchone()
        return dict(row) if row else None


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


def delete_product(product_id: str) -> bool:
    """
    Remove a product from the catalog (products + product_stock tables).
    Returns True if a row was actually deleted, False if not found.
    """
    with _lock, _connect() as conn:
        cur = _exec(conn, "DELETE FROM products WHERE id = ?", (product_id,))
        deleted = cur.rowcount > 0
        _exec(conn, "DELETE FROM product_stock WHERE product_id = ?", (product_id,))
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
    with _connect() as conn:
        # 1. If product has account inventory in product_accounts, use unsold count
        cur = _exec(
            conn,
            "SELECT COUNT(*) AS c FROM product_accounts WHERE product_id = ? AND is_sold = 0",
            (product_id,),
        )
        row = cur.fetchone()
        acc_count = int(row["c"]) if row else 0

        tot_cur = _exec(
            conn,
            "SELECT 1 FROM product_accounts WHERE product_id = ? LIMIT 1",
            (product_id,),
        )
        if tot_cur.fetchone() is not None:
            return acc_count

        # 2. Otherwise check product_stock table
        st_cur = _exec(
            conn,
            "SELECT stock FROM product_stock WHERE product_id = ?",
            (product_id,),
        )
        st_row = st_cur.fetchone()
        if st_row and st_row["stock"] is not None:
            return st_row["stock"]

        # 3. Fallback to products table
        pcur = _exec(
            conn,
            "SELECT stock FROM products WHERE id = ?",
            (product_id,),
        )
        prow = pcur.fetchone()
        return prow["stock"] if prow else None


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
        return True, new_stock


# --- Purchases / orders -----------------------------------------------------
def purchase(user_id: int, product: dict) -> dict:
    price = float(product["price"])
    pid = product["id"]
    now = int(time.time())

    with _lock, _connect() as conn:
        _exec(conn, "INSERT INTO users (user_id) VALUES (?) ON CONFLICT (user_id) DO NOTHING", (user_id,))

        # Check for available account in product_accounts
        acc_cur = _exec(
            conn,
            "SELECT id, account_data FROM product_accounts WHERE product_id = ? AND is_sold = 0 ORDER BY id ASC LIMIT 1",
            (pid,),
        )
        acc_row = acc_cur.fetchone()

        if acc_row:
            acc_id = acc_row["id"]
            delivery_text = acc_row["account_data"]
        else:
            acc_id = None
            delivery_text = product.get("delivery") or "Digital Item"

        # Check stock
        stock = get_stock(pid)
        if stock is not None and stock <= 0:
            return {"ok": False, "reason": "out_of_stock"}

        brow = _exec(
            conn,
            "SELECT balance FROM users WHERE user_id = ?",
            (user_id,),
        ).fetchone()
        balance = float(brow["balance"]) if brow else 0.0
        if balance < price:
            return {
                "ok": False,
                "reason": "insufficient",
                "balance": balance,
                "price": price,
            }

        # Deduct balance + count order
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
            cnt_cur = _exec(
                conn,
                "SELECT COUNT(*) AS c FROM product_accounts WHERE product_id = ? AND is_sold = 0",
                (pid,),
            )
            new_st = int(cnt_cur.fetchone()["c"])
            _exec(conn, "UPDATE products SET stock = ? WHERE id = ?", (new_st, pid))
            _exec(conn, "UPDATE product_stock SET stock = ? WHERE product_id = ?", (new_st, pid))
        elif stock is not None:
            _exec(conn, "UPDATE product_stock SET stock = stock - 1 WHERE product_id = ?", (pid,))
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

        new_balance = balance - price
        return {
            "ok": True,
            "order_id": order_id,
            "new_balance": new_balance,
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
