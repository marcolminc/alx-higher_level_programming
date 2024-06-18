#!/usr/bin/node
const str = 'C is fun';
const args = process.argv.slice(2);
let n = Number(args[0]);
if (isNaN(n)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < n; i++) {
    console.log(str);
  }
}
