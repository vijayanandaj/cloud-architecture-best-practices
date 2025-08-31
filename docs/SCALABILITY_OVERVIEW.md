# Scalability Overview

This repo contrasts **anti-patterns** with **good patterns** across four themes:
- Pagination
- API Gateway
- Caching
- Idempotency

Each example includes code and a README explaining:
- Why the anti-pattern fails (symptoms)
- The recommended approach
- What to measure when you run load tests later (p95/p99 latency, RPS, 429/504 rates, CPU/memory)
