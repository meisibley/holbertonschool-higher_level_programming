#!/usr/bin/node
const arg = parseInt(process.argv[2]);
function factorial (ar) {
  if (isNaN(ar) === true || ar === 1) {
    return (1);
  } else {
    return ar * factorial(ar - 1);
  }
}
console.log(factorial(arg));
