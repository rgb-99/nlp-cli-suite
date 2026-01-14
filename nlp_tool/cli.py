import click
from .ingest import ingest_cmd
from .benchmark import benchmark_cmd
from .report import report_cmd
from .suite_cmd import suite_cmd
from .compare_cmd import compare_cmd

@click.group()
def main():
    """Unified NLP infrastructure CLI."""
    pass

main.add_command(ingest_cmd)
main.add_command(benchmark_cmd)
main.add_command(report_cmd)
main.add_command(suite_cmd)
main.add_command(compare_cmd)

if __name__ == "__main__":
    main()