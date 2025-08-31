from fastapi import FastAPI, Request
import httpx
from labs.01_scalability.api_gateway.common.config import SLOW_UPSTREAM

app = FastAPI(title="Bad: direct calls")

@app.post("/price")
async def price_proxy(req: Request):
    payload = await req.body()
    async with httpx.AsyncClient() as client:
        # ❌ no timeout, no auth/limits → head-of-line blocking
        r = await client.post(SLOW_UPSTREAM, content=payload)
    return {"status": r.status_code, "len": len(r.text)}
