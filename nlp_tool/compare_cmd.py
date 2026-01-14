import click
from .compare import compare

@click.command("compare")
@click.argument("baseline", type=click.Path(exists=True))
@click.argument("current", type=click.Path(exists=True))
def compare_cmd(baseline, current):
    """
    Compare a CURRENT benchmark against a BASELINE.
    
    Identifies performance regressions in throughput, latency, and memory.
    """
    click.echo(f"🔍 Comparing {current} (current) vs {baseline} (baseline)...")
    
    try:
        diffs = compare(baseline, current)
        
        click.echo("\n" + "="*40)
        click.echo(f"📊 REGRESSION ANALYSIS")
        click.echo("-" * 40)

        # Logic for Throughput (Higher is better)
        t_color = "green" if diffs["throughput_delta"] >= 0 else "red"
        click.echo("Throughput Delta : ", nl=False)
        click.secho(f"{diffs['throughput_delta']:+.2f} tok/s", fg=t_color, bold=True)

        # Logic for Latency (Lower is better)
        l_color = "green" if diffs["latency_delta"] <= 0 else "red"
        click.echo("Latency Delta    : ", nl=False)
        click.secho(f"{diffs['latency_delta']:+.2f} ms", fg=l_color, bold=True)

        # Logic for Memory
        m_color = "green" if diffs["memory_delta"] <= 0 else "yellow"
        click.echo("Memory Delta     : ", nl=False)
        click.secho(f"{diffs['memory_delta']:+.2f} MB", fg=m_color)

        click.echo("="*40)

        # CI/CD Fail Condition: If throughput dropped by more than 5%
        # (This is where you'd add a sys.exit(1) for a real CI pipeline)

    except KeyError as e:
        click.secho(f"❌ Error: Missing expected metric in JSON: {e}", fg="red")
    except Exception as e:
        click.secho(f"❌ Error during comparison: {e}", fg="red")