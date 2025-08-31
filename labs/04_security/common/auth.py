from fastapi import HTTPException

def require_scope(required: set, token_scopes: set):
    if not required.issubset(token_scopes):
        raise HTTPException(403, "insufficient_scope")

def parse_token(header: str | None) -> set:
    # demo parser: "Bearer scope1,scope2"
    if not header or not header.lower().startswith("bearer"):
        return set()
    parts = header.split(None, 1)
    if len(parts) == 1: return set()
    scopes = {s.strip() for s in parts[1].split(",") if s.strip()}
    return scopes
