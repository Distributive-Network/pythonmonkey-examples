#!/usr/bin/env python3
"""
This example uses the JavaScript WebAssembly API to compile and
instantiate the `factorial.wasm` file and return the "fac" function
as a JavaScript promise.
"""

import asyncio
import pythonmonkey as pm

# get the global WebAssembly object
WebAssembly = pm.eval('WebAssembly')

async def async_fn():
  # read the factorial.wasm binary file
  file = open('factorial.wasm', 'rb')
  wasm_bytes = bytearray(file.read())

  # instantiate the WebAssemby code
  wasm_fact = await WebAssembly.instantiate(wasm_bytes, {})

  # return the "fac" factorial function fromn the wasm module
  return wasm_fact.instance.exports.fac;

# await the promise which returns the factorial WebAssembly function
factorial = asyncio.run(async_fn())

# execute WebAssembly code in Python!
print(factorial(4)) # this outputs "24.0" since factorial(4) == 24
print(factorial(5)) # this outputs "120.0"
print(factorial(6)) # this outputs "720.0"

