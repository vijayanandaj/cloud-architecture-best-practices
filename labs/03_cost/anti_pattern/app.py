from fastapi import FastAPI
app = FastAPI(title="Bad: all hot, chatty")

@app.post("/archive")
def archive(items: list[dict]):
    # ❌ stores everything to hot; writes one-by-one (many API calls)
    stored = [{"id": x.get("id"), "tier": "hot"} for x in items]
    return {"stored": stored, "calls": len(items)}
