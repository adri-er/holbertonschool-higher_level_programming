#!/usr/bin/node
const process = require('process');
const fs = require('fs');
const url = String(process.argv[2]);
const message = String(process.argv[3]);
fs.writeFile(url, message, 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
});
