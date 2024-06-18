#!/usr/bin/node
/*
 * counts number of args passed to the script
 * the first arg (arg[0]) is for the path to node.js executable
 * the second arg (arg[1]) is for the path to the js script
 * therefore, we skip the first two to end up with actual args
 * we use slice() for skipping the very first two pseudo-args
 */
const argsArray = process.argv.slice(2);
const argsCount = argsArray.length;
if (argsCount === 0) {
  console.log('No argument');
} else if (argsCount < 2) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
