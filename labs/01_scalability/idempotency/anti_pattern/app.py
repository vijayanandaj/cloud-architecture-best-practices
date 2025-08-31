from fastapi import FastAPI
import time

app = FastAPI(title="Bad: non-idempotent")
ORDERS = []

@app.post("/checkout")
def checkout(order: dict):
    # ❌ retries cause duplicate side-effects
    order["created_at"] = time.time()
    ORDERS.append(order)
    return {"ok": True, "order_id": len(ORDERS)}
