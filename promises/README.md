# Use JavaScript Promises in Python 

This example demonstrates using JavaScript promsies in Python with
Python's [asyncio library](https://docs.python.org/3/library/asyncio.html).

There are two files used in this example: `async-await-example.js` and
`main.py`.

`async-await-example.js` is a JavaScript module that contains a single
async function which returns a promise that resolves after 3 seconds
and returns the current unix time.

`main.py` is the entry point of this example. This program
demonstrates awaiting JavaScript promises defined from both `pm.eval()`
and from a JavaScript async function.

## Related Examples
Refer to the WebAssembly example for another example involving
awaiting JavaScript promises in Python.

