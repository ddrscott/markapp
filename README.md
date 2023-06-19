# Markapp

Literate Markdown for Apps™

This project helps generates `index.html`, `style.css`, and `script.js` from code blocks in Markdown files.

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

## Markdown Options

Here is a slightly more complex example.

    # Really Cool Prompt

    Make me a website with html, css, and javascript in their own files.
    
    ```html > index.html
    inner html
    ```
    
    ```css > css/style.css
    inner css
    ```
    
    ```javascript >> script/app.js
    inner javascript
    ```

## How to tell your generative AI to create these code blocks?!

Here is an example prompt to get you started:

> Your MUST respond with Literate Markdown. For example:
> - Each fenced code block must begin with three backticks followed by a language, space, greater than, space, and a file path.
> - You may append to a previous file by using two greater thans and then the file name.
> - Example create block:
>   ```javascript > src/index.js
>   console.log('hello')
>   ```
> - Example append block:
>   ```javascript >> src/index.js
```
