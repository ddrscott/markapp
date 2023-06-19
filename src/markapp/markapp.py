import os
import logging
import re

DEFAULT_OUTPUT = "docs"
DEFAULT_PORT = "8080"

DEFAULT_TYPE_TO_FILE = {
    "txt": "output.txt",
    "html": "index.html",
    "css": "style.css",
    "js": "script.js",
    "javascript": "script.js",
}

def extract_code_blocks(markdown_file):
    code_blocks = []

    found = None
    code = []
    with open(markdown_file, 'r') as f:
        for line in f:
            print(f"line: {line}")
            if not found:
                # find literate markdown fenched code blocks
                # - only the backticks are required.
                # - all other parts are optional.
                found = re.search(r"^```(?P<language>\w+)?\s*(?P<operation>\S+)?\s*(?P<file_path>\S+)?\s*$", line)
                if found:
                    code.clear()
            elif found and line.startswith('```'):
                file_type = found.group('language') or 'txt'
                operation = found.group('operation') or '>'
                file_path = found.group('file_path') or DEFAULT_TYPE_TO_FILE.get(file_type, DEFAULT_TYPE_TO_FILE['txt'])
                code_blocks.append({'text': ''.join(code), 'file_type': file_type, 'operation': operation, 'file_path': file_path})
                found = None
                code.clear()
            else:
                print(f"appending : {line}")
                code.append(line)

    return code_blocks

def compile(markdown_file, output_dir=DEFAULT_OUTPUT):
    logger = logging.getLogger(__name__)

    base_name = markdown_file.split('/')[-1].split('.')[0]
    full_dir = os.path.join(output_dir, base_name)

    logger.info(f"building {markdown_file} to {full_dir}")

    code_blocks = extract_code_blocks(markdown_file)
    for block in code_blocks:
        file_path = block['file_path']
        operation = block['operation']

        full_path = os.path.join(full_dir, file_path)
        dir_name = os.path.dirname(full_path)
        os.makedirs(dir_name, exist_ok=True)
        handle_operation(operation, full_path, block['text'])


def handle_operation(operation, file_path, content):
    logger = logging.getLogger(__name__)

    SUPPORTER_OPERATIONS = {
        '>' : op_write,
        '>>': op_append,
    }
    op = SUPPORTER_OPERATIONS.get(operation, None)
    if not op:
        raise Exception(f"Unsupported operation: {operation}")

    logger.info(f"handling operation: {operation} on {file_path}")
    op(file_path, content)


def op_write(file_path, content):
    logger = logging.getLogger(__name__)
    with open(file_path, 'w') as f:
        f.write(content)
        logger.info(f"writing {file_path}")

def op_append(file_path, content):
    logger = logging.getLogger(__name__)
    with open(file_path, 'a') as f:
        f.write(content)
        logger.info(f"appending {file_path}")

def serve(output_dir=DEFAULT_OUTPUT, host='0.0.0.0', port=8080):
    import http.server
    import socketserver
    import functools
    import logging

    Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=output_dir)

    logger = logging.getLogger(__name__)
    with socketserver.TCPServer((host, port), Handler) as httpd:
        logger.info(f"serving at {host}:{port}")
        httpd.serve_forever()
