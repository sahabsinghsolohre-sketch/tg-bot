"""
Watch incoming USDT (BEP20) transfers WITHOUT any API key.

Instead of BscScan's REST API, we talk directly to public Binance Smart Chain
RPC nodes using standard JSON-RPC. We read the USDT contract's `Transfer`
event logs where the recipient (`to`) is our wallet address.

This needs no signup and no key. Public nodes can rate-limit or go down, so we
rotate through several endpoints and cap how many blocks we scan per poll.

USDT Transfer event:
    Transfer(address indexed from, address indexed to, uint256 value)
    topic0 = keccak256("Transfer(address,address,uint256)")
"""

import logging

import requests

logger = logging.getLogger(__name__)

# USDT (BEP20) contract on Binance Smart Chain. 18 decimals.
USDT_CONTRACT = "0x55d398326f99059fF775485246999027B3197955"
USDT_DECIMALS = 18

# keccak256 of "Transfer(address,address,uint256)".
TRANSFER_TOPIC = (
    "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"
)

# Public BSC RPC endpoints (no key required) that allow eth_getLogs.
# Tried in order; we rotate on failure. Endpoints that demand an API key
# (e.g. Ankr's public URL for getLogs) are intentionally left out.
RPC_ENDPOINTS = [
    "https://bsc-dataseed.binance.org",
    "https://bsc-dataseed1.defibit.io",
    "https://bsc-dataseed1.ninicoin.io",
    "https://bsc-dataseed2.binance.org",
    "https://bsc-dataseed3.binance.org",
    "https://bsc-dataseed4.binance.org",
    "https://bsc.publicnode.com",
    "https://binance.llamarpc.com",
    "https://bsc-rpc.publicnode.com",
]

# BSC makes a block every ~3s. Cap the look-back so a poll stays cheap and
# stays within public nodes' getLogs range limits.
MAX_BLOCKS_LOOKBACK = 1000  # ~50 minutes of history

# Remember the RPC that worked last so we prefer it.
_preferred_rpc_index = 0


def _rpc_call(method: str, params: list):
    """Send a JSON-RPC call, rotating through endpoints until one answers."""
    global _preferred_rpc_index
    payload = {"jsonrpc": "2.0", "id": 1, "method": method, "params": params}

    order = list(range(len(RPC_ENDPOINTS)))
    # Try the last-known-good endpoint first.
    order.sort(key=lambda i: 0 if i == _preferred_rpc_index else 1)

    last_error = None
    for i in order:
        url = RPC_ENDPOINTS[i]
        try:
            resp = requests.post(url, json=payload, timeout=15)
            resp.raise_for_status()
            data = resp.json()
            if "error" in data:
                last_error = data["error"]
                logger.debug("RPC %s returned error: %s", url, data["error"])
                continue
            _preferred_rpc_index = i
            return data.get("result")
        except (requests.RequestException, ValueError) as exc:
            last_error = exc
            logger.debug("RPC %s failed: %s", url, exc)
            continue

    logger.warning("All BSC RPC endpoints failed. Last error: %s", last_error)
    return None


def _get_block_number() -> int:
    result = _rpc_call("eth_blockNumber", [])
    if result is None:
        return 0
    try:
        return int(result, 16)
    except (TypeError, ValueError):
        return 0


def get_latest_block() -> int:
    """Public helper: current chain head block number (0 if unavailable)."""
    return _get_block_number()


def _addr_to_topic(address: str) -> str:
    """Left-pad a 20-byte address to a 32-byte topic."""
    clean = address.lower().replace("0x", "")
    return "0x" + clean.rjust(64, "0")


def get_incoming_usdt_transfers(address: str, api_key: str = "", startblock: int = 0) -> list:
    """
    Return recent incoming USDT transfers to `address` via public BSC RPC.

    `api_key` is accepted but ignored (kept so the caller stays unchanged).

    Each item: {"amount": float, "tx_hash": str, "from": str, "block": int, "time": int}
    Returns an empty list on any error (logged) so polling can continue.
    """
    latest = _get_block_number()
    if latest == 0:
        return []

    from_block = max(0, latest - MAX_BLOCKS_LOOKBACK)

    # topic[0] = Transfer signature, topic[2] = indexed `to` = our address.
    # topic[1] (`from`) left as null to match any sender.
    log_filter = {
        "fromBlock": hex(from_block),
        "toBlock": hex(latest),
        "address": USDT_CONTRACT,
        "topics": [TRANSFER_TOPIC, None, _addr_to_topic(address)],
    }

    logs = _rpc_call("eth_getLogs", [log_filter])
    if not logs:
        return []

    transfers = []
    for log in logs:
        try:
            # `value` is the non-indexed event arg, carried in `data`.
            raw = int(log["data"], 16)
            amount = raw / (10 ** USDT_DECIMALS)
            # topics: [sig, from(padded), to(padded)]
            from_topic = log["topics"][1]
            from_addr = "0x" + from_topic[-40:]
            transfers.append(
                {
                    "amount": amount,
                    "tx_hash": log["transactionHash"],
                    "from": from_addr,
                    "block": int(log["blockNumber"], 16),
                    "time": 0,  # RPC logs don't include a timestamp; not needed.
                }
            )
        except (KeyError, ValueError, IndexError) as exc:
            logger.debug("Skipping malformed log: %s", exc)
            continue

    return transfers
