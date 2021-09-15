#!/usr/bin/node
const process = require('process');
const request = require('request');
const requestURL = String(process.argv[2]);

request(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    process.stdout.write('code: ');
    console.log(response.statusCode);
  }
});
