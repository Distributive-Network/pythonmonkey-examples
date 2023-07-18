# Load WebAssembly from Python

This example demonstrates running [WebAssembly](https://developer.mozilla.org/en-US/docs/WebAssembly) code from Python using
PythonMonkey.

There are two files used in this example: `factorial.wasm` and
`main.py`.

`factorial.wasm` is a WebAssembly binary program for calculating the
nth factorial. It exposes a function `fac(n)`.

`main.py` is the entry point of this example. This program reads 
`factorial.wasm` and uses JavaScript to compile and instantiate it.
Then it calls the `fac(n)` function directly from Python.

## Factorial Problem
For more information on Factorials, refer to [https://en.wikipedia.org/wiki/Factorial](https://en.wikipedia.org/wiki/Factorial)

## Factorial Source Code
Here is the source code for `factorial.wasm` written in WebAssembly
Text.

```wat
(module
  (func $fac (export "fac") (param f64) (result f64)
    local.get 0
    f64.const 1
    f64.lt
    if (result f64)
      f64.const 1
    else
      local.get 0
      local.get 0
      f64.const 1
      f64.sub
      call $fac
      f64.mul
    end))
```

