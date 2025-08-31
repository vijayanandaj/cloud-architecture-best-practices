from fastapi import FastAPI
app = FastAPI()
DATA = [{"id": i} for i in range(100_000)]  # huge

@app.get("/orders")
def orders():
    # ❌ BAD: unpaginated → big payloads, slow, memory spikes
    return {"items": DATA, "count": len(DATA)}
