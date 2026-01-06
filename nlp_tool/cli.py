import click
from .ingest import ingest_cmd
from .benchmark import benchmark_cmd
from .report import report_cmd

@click.group()
def main():
    """Unified NLP infrastructure CLI."""
    pass

main.add_command(ingest_cmd)
main.add_command(benchmark_cmd)
main.add_command(report_cmd)
