#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length <= 1) {
  console.log(0);
} else {
  const numerals = args.filter((e) => !isNaN(e)).map(Number);
  if (numerals.length <= 1) {
    console.log(0);
  } else {
    numerals.sort((a, b) => b - a);
    console.log(numerals[1]);
  }
}
