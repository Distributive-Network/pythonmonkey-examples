#!/usr/bin/env python3
"""

"""
import pythonmonkey as pm
require = pm.createRequire(__file__)

sha256 = require("./sha256")

print(sha256("Hello, World!"))

