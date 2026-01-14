import click
import json
import glob
import os

@click.command("report")
@click.argument("files", nargs=-1) # nargs=-1 allows multiple files
def report_cmd(files):
    """Compare multiple benchmark JSON files."""
    all_data = []

    # Handle multiple files or patterns like *.json
    for pattern in files:
        for filepath in glob.glob(pattern):
            if os.path.exists(filepath):
                with open(filepath, 'r') as f:
                    all_data.append(json.load(f))

    if not all_data:
        click.secho("❌ No benchmark files found to report.", fg="red")
        return

    # Sort by throughput (Highest speed first)
    all_data.sort(key=lambda x: x.get('throughput', 0), reverse=True)

    click.echo("\n🏆 MODEL PERFORMANCE RANKING")
    click.echo(f"{'Model Name':<25} | {'Speed (tok/s)':<15} | {'Memory (MB)':<10}")
    click.echo("-" * 55)

    for entry in all_data:
        # Use .get() to avoid KeyErrors
        name = entry.get('model', 'Unknown')
        tps = entry.get('throughput', 0.0)
        mem = entry.get('memory_mb', 0.0)
        click.echo(f"{name:<25} | {tps:<15.2f} | {mem:<10.1f}")