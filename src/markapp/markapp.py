import os
import logging

DEFAULT_OUTPUT = "docs"

DEFAULT_TYPE_TO_FILE = {
    "html": "index.html",
    "css": "style.css",
    "js": "script.js",
    "javascript": "script.js",
}

def extract_code_blocks(markdown_file):
    code_blocks = []
    with open(markdown_file, 'r') as f:
        for line in f:
            if line.startswith('```'):
                file_type = line.strip('`\n')
                code = ''
                for line in f:
                    if line.startswith('```'):
                        code_blocks.append({'text': code, 'file_type': file_type})
                        break
                    code += line
    return code_blocks

def compile(markdown_file, output_dir=DEFAULT_OUTPUT):
    logger = logging.getLogger(__name__)

    base_name = markdown_file.split('/')[-1].split('.')[0]
    full_dir = os.path.join(output_dir, base_name)

    logger.info(f"building {markdown_file} to {full_dir}")
    os.makedirs(full_dir, exist_ok=True)

    code_blocks = extract_code_blocks(markdown_file)
    for block in code_blocks:
        file_type = block['file_type']
        file_name = DEFAULT_TYPE_TO_FILE.get(file_type, None)
        if file_name:
            file_path = os.path.join(full_dir, file_name)
            with open(file_path, 'w') as f:
                f.write(block['text'])
                logger.info(f"writing {file_path}")
        else:
            logger.info(f"Ignoring block type: {file_type}")
