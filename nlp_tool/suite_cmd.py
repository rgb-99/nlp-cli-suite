
import click
from .suite_runner import run_suite

@click.command("suite")
@click.argument("file")
@click.option("--out-dir", help="Override output directory")
def suite_cmd(file, out_dir):
    run_suite(file, out_dir)
