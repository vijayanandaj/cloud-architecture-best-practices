from fastapi import FastAPI
from labs.01_scalability.cache.common.products import expensive

app = FastAPI(title="Bad: no cache")

@app.get("/product/{pid}")
def product(pid: int):
    # ❌ recompute every time → high latency and CPU
    return expensive(pid)
