#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  const data = JSON.parse(body);
  const usrs = {};
  for (const task of data) {
    if (task.completed) {
      if (usrs[task.userId]) {
        usrs[task.userId]++;
      } else {
        usrs[task.userId] = 1;
      }
    }
  }
  console.log(usrs);
});
