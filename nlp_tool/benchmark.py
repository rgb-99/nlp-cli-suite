import click
import subprocess

@click.command("benchmark")
@click.argument("model")
@click.option("--out", help="Save JSON result to a specific path")
def benchmark_cmd(model, out):
    """Benchmark a model via the hf-bench engine."""
    # Build the command list
    cmd = ["hf-bench", model]
    
    # If the user provided --out, pass it to the sub-tool
    if out:
        cmd += ["--out", out]
    
    click.echo(f"🚀 Running benchmark: {' '.join(cmd)}")
    subprocess.run(cmd)