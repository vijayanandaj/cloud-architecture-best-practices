from fastapi import FastAPI, Request
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time
from labs.06_observability.common.trace import new_correlation_id

app = FastAPI(title="Good: metrics + correlation ID")

REQS = Counter("http_requests_total","requests",["path","method","code"])
LAT  = Histogram("http_latency_ms","latency (ms)", buckets=(50,100,200,400,800,1600))

@app.middleware("http")
async def metrics_mw(request: Request, call_next):
    cid = request.headers.get("x-correlation-id") or new_correlation_id()
    start = time.perf_counter()
    response = await call_next(request)
    ms = (time.perf_counter() - start) * 1000
    REQS.labels(request.url.path, request.method, str(response.status_code)).inc()
    LAT.observe(ms)
    response.headers["x-correlation-id"] = cid
    return response

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

from fastapi import Response
@app.get("/do")
def do():
    return {"ok": True}
