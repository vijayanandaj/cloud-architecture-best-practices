# Idempotency — ❌ duplicates vs ✅ Idempotency-Key

## What this shows
- Safe retries under load balancers, queues, or flaky networks.

## Folders
- `anti_pattern/` → each retry applies side-effects again
- `good_pattern/` → returns the same result for the same Idempotency-Key

## Symptoms of the anti-pattern
- Double charges, duplicate rows, inconsistent state

## What the good pattern changes
- Duplicate submits with the same key are harmless
- Server remains safe under at-least-once delivery

## How you’d measure later
- Inject 3x retries per request; check duplicate rate
- Outbox consistency tests around checkout flow
