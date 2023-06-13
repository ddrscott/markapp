import click
import logging
from . import markapp

@click.command()
@click.argument('src')
@click.option('--output-dir', default='.', help='Output directory')
def cli(src, output_dir):
    markapp.compile(src, output_dir)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
    cli()
