#!/usr/bin/node
let prtCount = -1;
exports.logMe = function (item) {
  if (item) {
    prtCount++;
      console.log(prtCount + ': ' + item);
  }
};
