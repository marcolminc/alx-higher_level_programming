#!/usr/bin/node

const req = require('request');
const fs = require('fs');

req.get(process.argv[2], (e, res, body) => {
  if (e) {
    console.log(e);
  } else {
    fs.wrteFile(process.argv[3], body, 'utf-8', (e) => {
      if (e) {
        console.log(e);
      }
    });
  }
});
