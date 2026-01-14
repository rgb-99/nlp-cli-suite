import json

def compare(a, b):
    with open(a, 'r') as f_a, open(b, 'r') as f_b:
        base = json.load(f_a)
        curr = json.load(f_b)
        
    return {
        "throughput_delta": round(curr["throughput"] - base["throughput"], 2),
        "memory_delta": round(curr["memory_mb"] - base["memory_mb"], 2),
        "latency_delta": round(curr["latency_p50"] - base["latency_p50"], 2)
    }