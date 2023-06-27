#!/usr/bin/env python3
"""
This example uses the JavaScript WebAssembly API to compile and
instantiate the `factorial.wasm` file and return the "fac" function
as a JavaScript promise.
"""

import asyncio
import pythonmonkey as pm

async def async_fn():
  # open the factorial.wasm binary file
  file = open('factorial.wasm', 'rb')
  wasm_bytes = bytearray(file.read())

  # evaluate the JavaScript code and return the factorial function as
  # a JavaScript promise
  wasm_fact_function_promise = pm.eval('''
  async (code) => {
    const wasmFac = await WebAssembly.instantiate(code, {});
    return wasmFac.instance.exports.fac;
  }
  ''')

  return await wasm_fact_function_promise(wasm_bytes)

# await the promise which returns the factorial WebAssembly function
factorial = asyncio.run(async_fn())

# execute WebAssembly code in Python!
print(factorial(4)) # this outputs "24.0" since factorial(4) == 24
print(factorial(5)) # this outputs "120.0"
print(factorial(6)) # this outputs "720.0"

