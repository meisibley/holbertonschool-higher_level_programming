#!/usr/bin/node
const fs = require('fs');
const frFile = process.argv[2];
const writeTo = process.argv[3];

fs.writeFile(frFile, writeTo, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
