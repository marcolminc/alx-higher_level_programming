#!/usr/bin/node

const req = require('request');
const url = process.argv[2];
req.get(url, function (e, res) {
  if (e) {
    console.log(e);
  } else {
    console.log('code:' + ' ' + res.statusCode);
  }
});
