#!/usr/bin/node

const req = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

req.get(url, (e, res, body) => {
  if (e) {
    console.log(e);
  } else {
    const chars = JSON.parse(body).characters;
    for (const ch of chars) {
      req.get(ch, (e, res, body) => {
        if (e) {
          console.log(e);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
