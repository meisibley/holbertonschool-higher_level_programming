#!/usr/bin/node
if (isNaN(process.argv[2]) === true) {
  console.log('Missing size');
} else {
  for (let i = 1; i <= process.argv[2]; i++) {
    let printX = '';
    for (let j = 1; j <= process.argv[2]; j++) {
      printX += 'X';
    }
    console.log(printX);
  }
}
