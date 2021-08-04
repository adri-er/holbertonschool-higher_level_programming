#!/usr/bin/node
exports.esrever = function (list) {
  const listRev = [];
  for (let i = 0; i < list.length; i++) {
    listRev.push(list[list.length - i - 1]);
  }
  return listRev;
};
