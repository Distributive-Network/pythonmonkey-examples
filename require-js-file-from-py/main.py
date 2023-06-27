#!/usr/bin/env python3
import pythonmonkey as pm

require = pm.createRequire(__file__)
test = require('./my-javascript-module');
test.sayHello() # this outputs "hello, world"

