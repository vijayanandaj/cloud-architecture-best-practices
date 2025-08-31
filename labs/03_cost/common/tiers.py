def choose_tier(last_access_days: int) -> str:
    if last_access_days < 7: return "hot"
    if last_access_days < 90: return "warm"
    return "cold"

def estimate_monthly_cost(req_per_day: int, cost_per_req: float) -> float:
    return req_per_day * 30 * cost_per_req
