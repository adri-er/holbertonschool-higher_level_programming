#!/usr/bin/node
let amount = 0;
exports.logMe = function (item) {
  console.log(amount + ': ' + item);
  amount++;
};
