from fastapi import FastAPI
from labs.01_scalability.cache.common.products import expensive
import time, asyncio

app = FastAPI(title="Good: cache + singleflight")
CACHE = {}
LOCKS = {}

@app.get("/product/{pid}")
async def product(pid: int):
    now = time.time()
    v = CACHE.get(pid)
    if v and v["exp"] > now:
        return v["data"]
    lock = LOCKS.setdefault(pid, asyncio.Lock())
    async with lock:
        v = CACHE.get(pid)
        if v and v["exp"] > now:
            return v["data"]
        data = expensive(pid)
        CACHE[pid] = {"data": data, "exp": now + 15}  # TTL 15s
        return data
