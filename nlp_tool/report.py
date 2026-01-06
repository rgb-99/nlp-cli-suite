import click
import json
import os

@click.command("report")
@click.argument("files", nargs=-1) # Allows multiple files for comparison
def report_cmd(files):
    """Compare multiple benchmark results."""
    if not files:
        click.echo("❌ Please provide at least one benchmark JSON file.")
        return

    click.echo("\n📊 BENCHMARK COMPARISON REPORT")
    click.echo(f"{'Model Name':<20} | {'Tokens/Sec':<15} | {'Latency':<10}")
    click.echo("-" * 50)

    for file in files:
        if os.path.exists(file):
            with open(file, 'r') as f:
                data = json.load(f)
                # Assuming your benchmark output format from Project 2
                name = data.get("model", "Unknown")
                tps = data.get("tokens_per_sec", "N/A")
                lat = data.get("latency", "N/A")
                click.echo(f"{name:<20} | {tps:<15} | {lat:<10}")
        else:
            click.echo(f"⚠️  File {file} not found.")