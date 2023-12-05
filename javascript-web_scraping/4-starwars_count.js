#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const getData = JSON.parse(body).results;
    let count = 0;
    for (const mve in getData) {
      const character = getData[mve].characters;
      for (const chara in character) {
        if (character[chara].includes('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
