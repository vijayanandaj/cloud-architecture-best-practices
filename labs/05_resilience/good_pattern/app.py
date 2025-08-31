from fastapi import FastAPI, HTTPException
import asyncio, time
from labs.05_resilience.common.upstream import flaky_call

app = FastAPI(title="Good: circuit + bulkhead + fallback")
POOL = asyncio.Semaphore(10)  # bulkhead
CACHE = {"value": {"ok": True}, "ts": 0}

class Circuit:
    def __init__(self, failures=5, reset_s=5):
        self.failures, self.reset_s = failures, reset_s
        self.errs, self.state, self.open_at = 0, "closed", 0
    def allow(self):
        return not (self.state == "open" and time.time() < self.open_at + self.reset_s)
    def record(self, ok):
        if ok: self.errs = 0; 
        else:
            self.errs += 1
            if self.errs >= self.failures:
                self.state, self.open_at = "open", time.time()

CB = Circuit()

@app.get("/do")
async def do():
    if not CB.allow():
        # fallback to cached if circuit open
        return {"fallback": True, **CACHE["value"]}
    try:
        async with POOL:
            for attempt in range(3):
                try:
                    v = await flaky_call()
                    CACHE["value"], CACHE["ts"] = v, time.time()
                    CB.record(True)
                    return v
                except Exception:
                    await asyncio.sleep(0.05 * (2**attempt))
            CB.record(False)
            raise HTTPException(502, "upstream failed after retries")
    except HTTPException:
        raise
    except Exception:
        CB.record(False)
        raise HTTPException(502, "unexpected failure")
