import time, random
def expensive(pid: int):
    time.sleep(0.3)  # simulate slow compute/db
    return {"pid": pid, "price": round(100 + random.random(), 2)}
