import click
import subprocess

@click.command("benchmark")
@click.argument("model")
def benchmark_cmd(model):
    """Benchmark HuggingFace model."""
    subprocess.run(["hf-bench", model])
