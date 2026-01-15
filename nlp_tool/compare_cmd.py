import click
from .compare import compare_runs

@click.command("compare")
@click.argument("baseline", type=click.Path(exists=True))
@click.argument("current", type=click.Path(exists=True))
def compare_cmd(baseline, current):
    """Compare BASELINE folder results against CURRENT folder results."""
    report = compare_runs(baseline, current)

    click.secho("\n🚀 MODEL REGRESSION REPORT\n", bold=True, fg="cyan")
    header = f"{'Model':25} {'Speed Δ %':12} {'Memory Δ MB':15} Verdict"
    click.echo(header)
    click.echo("-" * len(header))

    for r in report:
        color = "green" if r["verdict"] == "IMPROVED" else "red"
        row = f"{r['model']:25} {r['speed_delta']:+11}% {r['memory_delta']:+14} MB  "
        click.echo(row, nl=False)
        click.secho(r["verdict"], fg=color, bold=True)