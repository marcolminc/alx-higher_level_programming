#!/usr/bin/node

const req = require('request');
let num = 0;

req.get(process.argv[2], (e, res, body) => {
  if (e) {
    console.log(e);
  } else {
    JSON.parse(body).results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(18)) {
          num++;
        }
      });
    });
    console.log(num);
  }
});
