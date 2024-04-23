# PythonMonkey Examples

## What is PythonMonkey
[PythonMonkey](https://pythonmonkey.io/) is a Python library for executing JavaScript in Python
and executing Python in JavaScript. It uses [Mozilla's SpiderMonkey](https://firefox-source-docs.mozilla.org/js/index.html)
JavaScript Engine and shares memory with Python for fast execution.

Check out [PythonMonkey on GitHub](https://github.com/Distributive-Network/PythonMonkey#pythonmonkey)!

## Installation
- requires Python 3.8 or higher
```bash
pip install pythonmonkey
```

## Running Examples
- Run the examples via `python3`. Refer to the README.md files in each of the directories for more information.

## Examples:
- `hello-world-eval.py`
  - A "Hello, World" which evaluates a string in JavaScript
  - Run with `python3 hello-world-eval.py`
- `function-call-eval.py`
  - Calling a JavaScript function in Python
  - Run with `python3 function-call-eval.py`
- `function-passing-eval.py`
  - Calling a Python function in a JavaScript function from Python
  - Run with `python3 function-passing-eval.py`
- `require-js-file-from-py/`
  - Loading a JavaScript module from Python
- `require-py-file-from-js/`
  - Loading a Python module from JavaScript
- `require-npm-package-from-py/`
  - Using an NPM package directly from Python
- `require-npm-packages/`
  - Calling JavaScript code that uses NPM modules
- `load-wasm-from-py/`
  - Loading a WebAssembly module in Python and calling WASM function
- `promises/`
  - Using JavaScript promises in Python

## Fullstack Example using CryptoJS
For a more in depth example using the CryptoJS NPM package, refer to [https://github.com/Distributive-Network/PythonMonkey-Crypto-JS-Fullstack-Example](https://github.com/Distributive-Network/PythonMonkey-Crypto-JS-Fullstack-Example/).
