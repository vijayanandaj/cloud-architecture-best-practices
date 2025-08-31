# Pagination — ❌ get-all vs ✅ cursor

## What this shows
- Why unpaginated endpoints cause slow responses, memory spikes and timeouts.
- How cursor pagination bounds work per request and gives stable continuation.

## Folders
- `common/` → `data.py` (10k rows)
- `anti_pattern/` → returns the whole list
- `good_pattern/` → cursor + `limit` (max 500)

## Symptoms of the anti-pattern
- p95/p99 latency grows with dataset size
- Big response sizes → increased egress $$
- Fragile retries (no stable position)

## What the good pattern changes
- Response size & work per request are bounded
- Stable paging during concurrent inserts/updates

## How you’d measure later
- p95/p99 latency with 1k–10k items
- Response size, memory profile
- Error rates under burst load (timeouts)
