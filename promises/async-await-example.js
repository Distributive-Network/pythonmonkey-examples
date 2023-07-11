/*
 * This function returns a JavaScript promise which resolves after
 * 3 seconds with the current unix timestamp in seconds.
 */
async function exampleAsyncFunc() {
  // create a promise that resolves in 3000 with the current date
  const somePromise = new Promise((resolve, reject) => {
      setTimeout(() => {
        resolve(new Date())
    }, 3000)
  });

  // await the promise defined above
  const time = await somePromise;

  // return the unix time in seconds
  return Math.trunc(time.getTime() / 1000);
}

module.exports = exampleAsyncFunc;

