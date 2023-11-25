#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    w = parseInt(w);
    h = parseInt(h);
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

Rectangle.prototype.print = function () {
  for (let row = 1; row <= this.height; row++) {
    const printX = 'X'.repeat(this.width);
    console.log(printX);
  }
};

module.exports = Rectangle;
