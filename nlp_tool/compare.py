import json
import os

def load_results(folder):
    data = {}
    for file in os.listdir(folder):
        if file.endswith(".json"):
            with open(os.path.join(folder, file)) as f:
                obj = json.load(f)
                data[obj["model"]] = obj
    return data

def compare_runs(baseline_dir, current_dir):
    base = load_results(baseline_dir)
    curr = load_results(current_dir)
    report = []

    for model in base:
        if model not in curr:
            continue

        b = base[model]
        c = curr[model]

        # Calculate percentage change for speed
        speed_delta = ((c["throughput"] - b["throughput"]) / b["throughput"]) * 100
        # Calculate absolute change for memory
        mem_delta = c["memory_mb"] - b["memory_mb"]

        # Improved = Faster + same or less memory
        verdict = "IMPROVED" if speed_delta > 0 and mem_delta <= 0 else "REGRESSED"

        report.append({
            "model": model,
            "speed_delta": round(speed_delta, 2),
            "memory_delta": round(mem_delta, 2),
            "verdict": verdict
        })
    return report