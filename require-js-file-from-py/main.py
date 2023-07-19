#!/usr/bin/env python3
import pythonmonkey as pm

test = pm.require('./my-javascript-module');
test.sayHello() # this outputs "hello, world"

