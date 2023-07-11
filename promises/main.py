#!/usr/bin/env python3
"""
This example demonstrates JavaScript promises interacting with Python
using Python's asyncio library.

For an additional example using a real world example of promises,
refer to the WebAssembly example.
"""
import pythonmonkey as pm
import asyncio
import time

require = pm.createRequire(__file__)
async_await_example = require("./async-await-example")

async def main():
  # create a JavaScript promise which resolves after 1 second (1000 milliseconds)
  my_awesome_promise = pm.eval("new Promise((resolve, reject) => { setTimeout(resolve, 1000); })")
  await my_awesome_promise # await the promise
  print("1 second later") # this will output one second after the line above was invoked

  # This example awaits another promise that returns the current time after 3 seconds
  print(int(time.time())) # will output the current unix time in seconds
  current_unix_time = await async_await_example() # awaits for 3 seconds
  print(current_unix_time) # will output the current unix time in seconds

asyncio.run(main())

