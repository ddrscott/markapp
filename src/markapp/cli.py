import click
import logging
import os
import glob
import concurrent.futures

from . import markapp, watcher

@click.command()
@click.argument('src')
@click.option('--output-dir', default='.', help='Output directory')
@click.option('--watch', is_flag=True, help='Watch for changes and recompile')
@click.option('--debounce', default=500, help='Debounce time in milliseconds')
@click.option('--serve', is_flag=True, help='Serve the output directory')
@click.option('--host', default='0.0.0.0', help='Serve host')
@click.option('--port', default=8080, help='Serve port')
def cli(src, output_dir, watch, debounce, serve, host, port):
    """Compile markdown files into HTML"""

    if os.path.isdir(src):
        glob_pattern = os.path.join(src, '*.md')
        for path in glob.glob(glob_pattern):
            click.echo(f'compiling: {path} -> {output_dir}')
            markapp.compile(path, output_dir)
    elif os.path.isfile(src):
        click.echo(f'compiling: {src} -> {output_dir}')
        markapp.compile(src, output_dir)
    else:
        raise ValueError(f'Invalid source path: {src}')

    futures = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        if watch:
            def on_change(path):
                click.echo(f'compiling: {path} -> {output_dir}')
                markapp.compile(path, output_dir)
            futures.append(executor.submit(watcher.watch, on_change=on_change, path=src, debounce_ms=debounce))

        if serve:
            click.echo(f'serving {output_dir} on {host}:{port}')
            futures.append(executor.submit(markapp.serve, output_dir, host, port))

        # Wait for both functions to finish
        if futures:
            print('Press Ctrl+C to exit')
            concurrent.futures.wait(futures)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
    cli()
