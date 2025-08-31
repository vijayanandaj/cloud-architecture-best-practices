from fastapi import FastAPI
from labs.01_scalability.pagination.common.data import DATA

app = FastAPI(title="Bad: unpaginated list")

@app.get("/orders")
def orders():
    # ❌ returns everything → huge payloads, slow, memory spikes
    return {"items": DATA, "count": len(DATA)}
