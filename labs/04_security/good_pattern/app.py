from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from labs.04_security.common.auth import parse_token, require_scope

app = FastAPI(title="Good: scoped access + narrow CORS")
app.add_middleware(CORSMiddleware, allow_origins=["https://app.example.com"], allow_methods=["GET"], allow_headers=["Authorization"])

@app.get("/orders")
def orders(req: Request):
    scopes = parse_token(req.headers.get("authorization"))
    if not scopes:
        raise HTTPException(401, "missing/invalid token")
    require_scope({"orders:read"}, scopes)
    return [{"id": 1, "total": 42.0}]
