#!/usr/bin/node
exports.esrever = function (list) {
  const result = [];
  let j = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    result[j] = list[i];
    j++;
  }
  return result;
};
