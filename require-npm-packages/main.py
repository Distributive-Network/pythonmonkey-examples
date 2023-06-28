#!/usr/bin/env python3
"""
This example requires a JavaScript file that itself requires an NPM
module called CryptoJS. That file exports a function called `sha256`
which will return the sha256 hash of a string entered.
"""
import pythonmonkey as pm
require = pm.createRequire(__file__)

sha256 = require("./sha256")

print(sha256("Hello, World!")) # this outputs dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f

