# Scalability Labs (Anti-patterns vs Good Patterns)

Each example has:
- `common/`: tiny helpers shared by both variants
- `anti_pattern/`: deliberately “usual/bad” code to surface problems
- `good_pattern/`: a recommended implementation

## Topics
1. **Pagination** — ❌ get-all vs ✅ cursor pagination
2. **API Gateway** — ❌ direct slow calls vs ✅ gateway (auth, rate limit, timeout)
3. **Caching** — ❌ recompute every hit vs ✅ cache + stampede protection
4. **Idempotency** — ❌ duplicate side-effects vs ✅ Idempotency-Key

> These are teaching artifacts. You can run them later with FastAPI/Uvicorn; for now, read the code + README in each folder.
