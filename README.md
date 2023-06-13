# Markapp

Generates `index.html`, `style.css`, and `script.js` from code blocks in Markdown files.

Generative AI is all the rage, but it can be cumbersome to try out code that it generates.
This script allows us to manages notes and code snippets in a single file and
break them up into multiple files for easy web serving.

## Example Usage

```sh
pip install https://github.com/ddrscott/markapp.get

markapp sample.md --output-dir .

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
    inner javascipt
    ```
