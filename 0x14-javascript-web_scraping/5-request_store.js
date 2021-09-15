#!/usr/bin/node
const process = require('process');
const request = require('request');
const fs = require('fs');
const requestURL = String(process.argv[2]);
const pathStore = String(process.argv[3]);

request(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(pathStore, body, 'utf8', function (err, data) {
      if (err) {
        return console.log(err);
      }
    }
    );
  }
});
