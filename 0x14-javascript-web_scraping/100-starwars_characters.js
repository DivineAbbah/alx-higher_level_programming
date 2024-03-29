#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;
  for (const cha of characters) {
    request(cha, (error, res, body) => {
      if (error) {
        console.log(error);
        return;
      }
      const characterJson = JSON.parse(body);
      console.log(characterJson.name);
    });
  }
});
