from fastapi import FastAPI
app = FastAPI(title="Bad: prints only")

@app.get("/do")
def do():
    print("processing request")  # ❌ hard to correlate
    return {"ok": True}
