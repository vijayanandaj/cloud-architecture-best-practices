from fastapi import FastAPI
import asyncio, httpx
from labs.02_performance.common.endpoints import ENDPOINTS

app = FastAPI(title="Good: async fan-out with budget & cap")

MAX_CONCURRENCY = 5
TIME_BUDGET_S = 0.8

@app.get("/aggregate")
async def aggregate():
    sem = asyncio.Semaphore(MAX_CONCURRENCY)
    async def fetch(url):
        async with sem:
            try:
                async with httpx.AsyncClient(timeout=TIME_BUDGET_S) as c:
                    r = await c.get(url)
                    return {"url": url, "status": r.status_code}
            except httpx.TimeoutException:
                return {"url": url, "status": "timeout"}
    results = await asyncio.gather(*(fetch(u) for u in ENDPOINTS))
    return {"results": results, "budget_s": TIME_BUDGET_S}
