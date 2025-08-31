# Security — ❌ no auth & wide CORS vs ✅ scoped auth & least privilege

**Anti-pattern:** endpoints readable by anyone; `Access-Control-Allow-Origin: *`.  
**Good pattern:** **scoped** Bearer token (or API key) and **narrow CORS**.

**Folders**
- `common/` → simple scope parser & checker
- `anti_pattern/` → anonymous, permissive CORS
- `good_pattern/` → scope-checked, narrow CORS

**What to discuss later:** rotate secrets, mTLS, fine-grained policies (OPA), input validation.
