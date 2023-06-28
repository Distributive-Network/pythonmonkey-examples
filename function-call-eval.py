#!/usr/bin/env python3
"""
This example demonstrates calling a JavaScript function from Python.
A simple function is defined in JavaScript which just returns the
number 3.
"""

import pythonmonkey as pm
my_JS_function = pm.eval(" () => { return 3; }")
print(my_JS_function())

