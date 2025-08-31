# Cost — ❌ always hot & chatty vs ✅ tiering & batching

**Anti-pattern:** put all data on hot storage and make per-item API calls.  
**Good pattern:** route **hot/warm/cold** by recency and **batch** to cut calls.

**Folders**
- `common/` → tier chooser + simple cost est.
- `anti_pattern/` → hot + one-by-one
- `good_pattern/` → tiered + batched

**What to measure later:** API calls saved, storage mix %, est. monthly cost.
