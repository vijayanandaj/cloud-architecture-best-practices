from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Bad: no auth, wide open CORS")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/orders")
def orders():
    # ❌ anyone can read; no scopes; PII risk
    return [{"id": 1, "total": 42.0}]

