from fastapi import FastAPI
from labs.03_cost.common.tiers import choose_tier, estimate_monthly_cost

app = FastAPI(title="Good: tiered + batch")

@app.post("/archive")
def archive(items: list[dict]):
    # ✅ choose tier per item; batch per tier (fewer calls)
    buckets = {"hot": [], "warm": [], "cold": []}
    for x in items:
        days = int(x.get("last_access_days", 0))
        buckets[choose_tier(days)].append(x.get("id"))
    calls = sum(1 for k,v in buckets.items() if v)  # 1 call per non-empty tier
    return {"buckets": {k: len(v) for k,v in buckets.items()}, "calls": calls}

@app.get("/cost")
def cost(req_per_day: int = 100000, cost_per_req: float = 0.000002):
    return {"monthly_usd": estimate_monthly_cost(req_per_day, cost_per_req)}
