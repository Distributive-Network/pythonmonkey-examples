#!/usr/bin/env python3
"""
This example demonstrates passing functions as arguments. Here, a
function is deinfed in JavaScript which expects a function as an
argument. Then that JavaScript function is executed from Python and
the Python `print` function  is passed as an argument.
"""

import pythonmonkey as pm
hello = pm.eval("(func) => { func('Hello, World!'); }")
hello(print) # this outputs "Hello, World!"

