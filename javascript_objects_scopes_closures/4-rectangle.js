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

Rectangle.prototype.double = function () {
  this.width *= 2;
  this.height *= 2;
};

Rectangle.prototype.rotate = function () {
  let swtch = this.width;
  this.width = this.height;
  this.height = swtch;
};

module.exports = Rectangle;
