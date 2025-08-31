# Performance — ❌ sequential fan-out vs ✅ async with time budgets

**Anti-pattern:** sequential upstream calls with no timeouts → one slow hop stalls the whole request.  
**Good pattern:** fire in parallel with a **timeout budget** and a **concurrency cap**.

**Folders**
- `common/` → `ENDPOINTS` list
- `anti_pattern/` → blocking, no timeouts
- `good_pattern/` → asyncio + httpx.AsyncClient with budget

**What to measure later:** p95 latency, tail timeouts, concurrency vs. RPS.
