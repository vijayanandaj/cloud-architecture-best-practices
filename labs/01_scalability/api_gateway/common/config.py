# httpbin simulates latency: /delay/2 sleeps 2s, /delay/0.5 sleeps 0.5s
SLOW_UPSTREAM = "https://httpbin.org/delay/2"
FAST_UPSTREAM = "https://httpbin.org/delay/0.5"
MAX_BODY = 64_000  # bytes
