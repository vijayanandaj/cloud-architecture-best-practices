from fastapi import FastAPI
import httpx
from labs.02_performance.common.endpoints import ENDPOINTS

app = FastAPI(title="Bad: sequential fan-out, no timeouts")

@app.get("/aggregate")
def aggregate():
    # ❌ Calls each upstream one-by-one; single slow hop delays all
    out = []
    with httpx.Client() as c:
        for url in ENDPOINTS:
            r = c.get(url)  # no timeout; may hang
            out.append({"url": url, "status": r.status_code})
    return {"results": out}
