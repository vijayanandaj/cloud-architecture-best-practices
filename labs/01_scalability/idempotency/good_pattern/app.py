from fastapi import FastAPI, Header, HTTPException
import time

app = FastAPI(title="Good: idempotency key")
ORDERS = []
MEMO = {}  # key -> response

@app.post("/checkout")
def checkout(order: dict, idempotency_key: str = Header(default=None, convert_underscores=False)):
    if not idempotency_key:
        raise HTTPException(400, "Missing Idempotency-Key header")
    if idempotency_key in MEMO:
        return MEMO[idempotency_key]
    order["created_at"] = time.time()
    ORDERS.append(order)
    resp = {"ok": True, "order_id": len(ORDERS)}
    MEMO[idempotency_key] = resp
    return resp
