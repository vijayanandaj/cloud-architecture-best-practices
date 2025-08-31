import random, asyncio
async def flaky_call():
    await asyncio.sleep(random.uniform(0.05, 0.2))
    if random.random() < 0.3:
        raise RuntimeError("upstream error")
    return {"ok": True}

