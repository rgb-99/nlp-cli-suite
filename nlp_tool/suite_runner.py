import subprocess
import os
import yaml
import click

def run_suite(path, out_override=None):
    with open(path, "r") as f:
        suite = yaml.safe_load(f)

    out_dir = out_override or suite.get("out_dir", "results")
    os.makedirs(out_dir, exist_ok=True)

    click.secho(f"📋 Running Suite: {path}", fg="cyan", bold=True)

    tokens = suite.get("tokens", 32)
    models = suite["models"]

    for m in models:
        fname = m.replace("/", "_") + ".json"
        out = os.path.join(out_dir, fname)
        click.secho(f"→ {m}", fg="yellow")
        subprocess.run(["hf-bench", m, "--tokens", str(tokens), "--out", out])
