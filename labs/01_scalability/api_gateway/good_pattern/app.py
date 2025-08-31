from fastapi import FastAPI, Request, HTTPException
import time, httpx
from labs.01_scalability.api_gateway.common.config import FAST_UPSTREAM, MAX_BODY

app = FastAPI(title="Good: API Gateway")
API_KEYS = {"secret-123"}  # demo only
buckets = {}  # ip -> (tokens, ts)
RATE, BURST = 5.0, 10

def allow(ip):
    tokens, ts = buckets.get(ip, (BURST, time.monotonic()))
    now = time.monotonic()
    tokens = min(BURST, tokens + (now - ts) * RATE)
    if tokens >= 1:
        buckets[ip] = (tokens - 1, now)
        return True
    buckets[ip] = (tokens, now)
    return False

@app.post("/price")
async def price_proxy(req: Request):
    if req.headers.get("x-api-key") not in API_KEYS:
        raise HTTPException(401, "missing/invalid api key")
    body = await req.body()
    if len(body) > MAX_BODY:
        raise HTTPException(413, "payload too large")
    ip = req.client.host if req.client else "unknown"
    if not allow(ip):
        raise HTTPException(429, "rate limit")
    timeout = httpx.Timeout(1.0)
    async with httpx.AsyncClient(timeout=timeout) as client:
        try:
            r = await client.post(FAST_UPSTREAM, content=body)
            return {"status": r.status_code, "len": len(r.text)}
        except httpx.TimeoutException:
            raise HTTPException(504, "upstream timeout")
