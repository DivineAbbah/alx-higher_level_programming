#!/usr/bin/node

/*  computes the number of the tasks completed by user id. */

const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) console.log(err);
  else {
    const dict = {};
    const json = JSON.parse(body);
    for (let i = 0; i < json.length; i++) {
      if (json[i].completed === true) {
        if (dict[json[i].userId] === undefined) {
          dict[json[i].userId] = 0;
        }
        dict[json[i].userId]++;
      }
    }
    console.log(dict);
  }
});
