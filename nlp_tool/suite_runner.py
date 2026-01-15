from concurrent.futures import ThreadPoolExecutor, as_completed

import subprocess
import os
import yaml
import click

def run_suite(path, out_override=None):
    with open(path, "r") as f:
        suite = yaml.safe_load(f)

    models = suite["models"]
    tokens = suite.get("tokens", 32)
    parallel = suite.get("parallel", 1)

    out_dir = out_override or suite.get("out_dir", "results")
    os.makedirs(out_dir, exist_ok=True)

    click.secho(f"📋 Running Suite with {parallel} workers", fg="cyan", bold=True)

    def run_model(model):
        out_file = os.path.join(out_dir, model.replace("/", "_") + ".json")
        subprocess.run(["nlp-tool", "benchmark", model, "--num-tokens", str(tokens), "--out", out_file])

    with ThreadPoolExecutor(max_workers=parallel) as pool:
        futures = [pool.submit(run_model, m) for m in models]
        for f in as_completed(futures):
            pass
