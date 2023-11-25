#!/usr/bin/node
const array = process.argv;
if (array.length < 4) {
  console.log(0);
} else {
  array.splice(0, 2);
  const arrInt = array.map(Number);
  const arrIndex = arrInt.indexOf(Math.max(...arrInt));
  arrInt.splice(arrIndex, 1);
  console.log(Math.max(...arrInt));
}
