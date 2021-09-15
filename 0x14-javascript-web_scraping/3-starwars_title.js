#!/usr/bin/node
const process = require('process');
const request = require('request');
const requestURL = 'https://swapi-api.hbtn.io/api/films/' + String(process.argv[2]) + '/';

request(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
