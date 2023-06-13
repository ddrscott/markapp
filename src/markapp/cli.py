import click
import logging
from . import markapp

@click.group()
def cli():
    pass

@cli.command()
@click.argument('src')
@click.option('--output-dir', default='.', help='Output directory')
def build(src, output_dir):
    markapp.compile(src, output_dir)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
    cli()
