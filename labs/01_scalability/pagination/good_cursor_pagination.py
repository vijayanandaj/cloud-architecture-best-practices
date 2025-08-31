from fastapi import FastAPI, HTTPException
from typing import Optional
import base64, json

app = FastAPI()
DATA = [{"id": i} for i in range(10_000)]

def encode_cursor(idx: int) -> str:
    return base64.urlsafe_b64encode(json.dumps({"i": idx}).encode()).decode()

def decode_cursor(cur: str) -> int:
    try:
        return json.loads(base64.urlsafe_b64decode(cur.encode()).decode())["i"]
    except Exception:
        raise HTTPException(400, "bad cursor")

@app.get("/orders")
def orders(limit: int = 100, cursor: Optional[str] = None):
    start = decode_cursor(cursor) if cursor else 0
    end = min(start + max(1, min(limit, 500)), len(DATA))
    items = DATA[start:end]
    next_cur = encode_cursor(end) if end < len(DATA) else None
    return {"items": items, "next_cursor": next_cur, "count": len(items)}
