#!/usr/bin/node
const process = require('process');
const fs = require('fs');
fs.readFile(String(process.argv[2]), 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
