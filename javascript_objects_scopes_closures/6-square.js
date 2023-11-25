#!/usr/bin/node
const SquareA = require('./5-square');

class Square extends SquareA {
  charPrint (c) {
    let printChar = c;
    if (typeof c === 'undefined') {
      printChar = 'X';
    }
    for (let row = 1; row <= this.height; row++) {
      const printX = printChar.repeat(this.width);
      console.log(printX);
    }
  }
}
module.exports = Square;
