#!/usr/bin/node

const req = require('request');

req.get(process.argv[2], { json: true }, (e, res, body) => {
  if (e) {
    console.log(e);
    return;
  }
  const doneTasks = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!doneTasks[todo.userId]) {
        doneTasks[todo.userId] = 1;
      } else {
        doneTasks[todo.userId] += 1;
      }
    }
  });
  console.log(doneTasks);
});
