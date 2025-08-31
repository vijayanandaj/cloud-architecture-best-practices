from fastapi import FastAPI
from labs.05_resilience.common.upstream import flaky_call

app = FastAPI(title="Bad: no timeout, no retry")

@app.get("/do")
async def do():
    # ❌ fails often; no isolation or fallback
    return await flaky_call()
