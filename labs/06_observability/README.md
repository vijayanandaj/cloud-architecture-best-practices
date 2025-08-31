# Observability — ❌ prints vs ✅ metrics + correlation IDs

**Anti-pattern:** only `print` logs; no metrics; can’t correlate requests.  
**Good pattern:** Prometheus **counters/histograms** and **correlation IDs**.

**Folders**
- `common/` → correlation ID helper
- `anti_pattern/` → prints only
- `good_pattern/` → `/metrics` endpoint + middleware adding `x-correlation-id`

**What to measure later:** request counts, latency histograms, traceability across services.
