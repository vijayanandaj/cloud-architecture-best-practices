# Caching — ❌ recompute vs ✅ cache + singleflight

## What this shows
- Reduce hot-path latency and CPU by caching.
- Avoid thundering herds with a singleflight lock.

## Folders
- `common/` → slow function to simulate DB/compute
- `anti_pattern/` → recomputes for every request
- `good_pattern/` → TTL cache + per-key async lock

## Symptoms of the anti-pattern
- p95 latency dominated by recompute
- CPU waste; poor throughput

## What the good pattern changes
- Cache hits return at memory speed
- Only 1 request populates a cold key (others wait)

## How you’d measure later
- Hit ratio, p95/p99 latency under load
- CPU time, RPS scaling with cache enabled
