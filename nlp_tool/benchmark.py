import click
import subprocess

@click.command("benchmark")
@click.argument("model")
@click.option("--num-tokens", default=32, type=int, help="Number of tokens to generate")
@click.option("--out", help="Save JSON result to a specific path")
def benchmark_cmd(model, num_tokens, out):
    """Benchmark a model via the hf-bench engine."""
    # Build the command list
    cmd = ["hf-bench", model, "--tokens", str(num_tokens)]
    
    # If the user provided --out, pass it to the sub-tool
    if out:
        cmd += ["--out", out]
    
    click.echo(f"🚀 Running benchmark: {' '.join(cmd)}")
    subprocess.run(cmd)