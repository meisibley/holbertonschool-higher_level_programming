#!/usr/bin/node
if ((isNaN(process.argv[2]) === true) || (isNaN(process.argv[3]) === true)) {
  console.log('NaN');
} else {
  console.log(Number(process.argv[2]) + Number(process.argv[3]));
}
