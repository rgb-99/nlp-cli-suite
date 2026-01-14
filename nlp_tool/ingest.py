import click
import subprocess

@click.command("ingest")
@click.argument("path")
def ingest_cmd(path):
    """Ingest and clean raw datasets."""
    subprocess.run(["nlp-engine", "ingest", path])
