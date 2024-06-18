#!/usr/bin/node
const str = 'C is fun';
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing number of occurences');
} else {
  const n = Number(process.argv[2]);
  for (let i = 0; i < n; i++) {
    console.log(str);
  }
}
