#!/usr/bin/node
const process = require('process');
const request = require('request');
const requestURL = String(process.argv[2]).slice(0, -5) + 'people/18/';

request(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).films.length);
  }
});
