import csv
import json
import os
import click

@click.command("export")
@click.argument("results_dir", type=click.Path(exists=True))
@click.argument("out_csv")
def export_cmd(results_dir, out_csv):
    """Export benchmark JSON results into a CSV table."""
    rows = []
    # Loop through the directory you specified
    for f in os.listdir(results_dir):
        if not f.endswith(".json"):
            continue
        
        with open(os.path.join(results_dir, f)) as json_file:
            data = json.load(json_file)
            rows.append([
                data["model"],
                data["throughput"],
                data["latency_p50"],
                data["memory_mb"]
            ])

    with open(out_csv, "w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["model", "throughput", "latency_ms", "memory_mb"])
        writer.writerows(rows)

    click.secho(f"📁 Exported {len(rows)} rows to {out_csv}", fg="green", bold=True)