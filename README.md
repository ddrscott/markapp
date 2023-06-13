# Markapp

Generates `index.html`, `style.css`, and `script.js` from code blocks in Markdown files.

Generative AI is all the rage, but it can be cumbersome to try out code that it generates.
This script allows us to manages notes and code snippets in a single file and
break them up into multiple files for easy web serving.

## Example Usage

```sh
pip install markapp

# Get list of options
markapp --help

#   Usage: markapp [OPTIONS] SRC
#   
#     Compile markdown files into HTML
#   
#   Options:
#     --output-dir TEXT   Output directory
#     --watch             Watch for changes and recompile
#     --debounce INTEGER  Debounce time in milliseconds
#     --serve             Serve the output directory
#     --host TEXT         Serve host
#     --port INTEGER      Serve port
#     --help              Show this message and exit.
#     Compile markdown files into HTML

markapp tests/sample.md --output-dir .

# Will generate `sample` directory with the following structure:
tree sample
#  sample
#  ├── index.html
#  ├── script.js
#  └── style.css
```

## Sample Markdown

    # Really Cool Prompt

    Make me a website with html, css, and javascript in their own files.
    
    ```html
    inner html
    ```
    
    ```css
    inner css
    ```
    
    ```javascript
    inner javascript
    ```
