#!/usr/bin/env python3
"""
This example returns a "HELLO, WORLD!" string created in JavaScript
using `pm.eval` for execting the JavaScript code.
The string is set to uppercase using JavaScript's `toUpperCase`
function.
"""

import pythonmonkey as pm
hello = pm.eval(" 'Hello, World!'.toUpperCase(); ")
print(hello) # this outputs "HELLO, WORLD!"

