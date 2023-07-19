#!/usr/bin/env python3
"""
This example demonstrates requiring an NPM package from Python. The
"is-odd" (https://www.npmjs.com/package/is-odd) is used. Please refer
to the README file in this directory for instructions on how to
install it.
"""

import pythonmonkey as pm

isOdd = pm.require("is-odd")

print(isOdd(7)) # This will output False
print(isOdd(2048)) # This will output True

