import click
import logging
import os
import glob
from . import markapp, watcher

@click.command()
@click.argument('src')
@click.option('--output-dir', default='.', help='Output directory')
@click.option('--watch', is_flag=True, help='Watch for changes and recompile')
@click.option('--debounce', default=500, help='Debounce time in milliseconds')
def cli(src, output_dir, watch, debounce):
    """Compile markdown files into HTML"""

    if os.path.isdir(src):
        glob_pattern = os.path.join(src, '*.md')
        for path in glob.glob(glob_pattern):
            markapp.compile(path, output_dir)
    elif os.path.isfile(src):
        markapp.compile(src, output_dir)
    else:
        raise ValueError(f'Invalid source path: {src}')

    if watch:
        def on_change(path):
            markapp.compile(path, output_dir)
        watcher.watch(on_change=on_change, path=src, debounce_ms=debounce)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
    cli()
