
# API Gateway — ❌ direct vs ✅ gateway

## What this shows
- Why fronting services with a gateway improves **load shaping** and **safety**.

## Folders
- `common/` → config (max body, upstreams)
- `anti_pattern/` → direct calls to slow upstream
- `good_pattern/` → API key, per-client rate limiting, size guard, timeout

## Symptoms of the anti-pattern
- Head-of-line blocking (no timeouts)
- No backpressure → upstream meltdown
- No auth/rate-limit → noisy neighbors

## What the good pattern changes
- **Auth** gate, **rate limits**, **payload limits**
- **Timeouts** and controlled retries around upstreams

## How you’d measure later
- p95 latency under burst load
- 429 rate (rate-limit behavior)
- 504s avoided via enforced timeouts
