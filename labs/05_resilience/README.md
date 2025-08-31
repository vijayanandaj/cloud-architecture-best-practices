# Resilience — ❌ direct & brittle vs ✅ circuit, bulkhead, fallback

**Anti-pattern:** straight call to flaky dependency; cascades failures.  
**Good pattern:** **bulkhead** (semaphore), **retries with backoff**, **circuit breaker**, and **fallback** to last good.

**Folders**
- `common/` → flaky upstream
- `anti_pattern/` → no isolation
- `good_pattern/` → breaker + backoff + cache fallback

**What to measure later:** error rates, time to recovery, saturation under chaos (kill upstream).
