#!/usr/bin/node
/* prints title of a star movie based on the id */

const request = require('request');
const id = process.argv[2];
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';

request(apiUrl + id + '/', (err, response, body) => {
  if (err) console.log(err);
  else console.log(JSON.parse(body).title);
});
