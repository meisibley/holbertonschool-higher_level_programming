#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let elementCount = 0;
  for (let i = 1; i <= list.length; i++) {
    if (list[i - 1] === searchElement) {
      elementCount++;
    }
  }
  return elementCount;
};
