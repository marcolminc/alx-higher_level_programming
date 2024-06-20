#!/usr/bin/node
const dict = require('./101-data').dict;
const uniqueIds = Array.from(new Set(Object.values(dict)));
const keys = Object.keys(dict);
const resultDict = {};
for (const id of uniqueIds) {
  const list = [];
  for (const key of keys) {
    if (dict[key] === id) {
      list.push(key);
    }
  }
  resultDict[id] = list;
}
console.log(resultDict);
