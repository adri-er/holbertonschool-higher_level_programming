#!/usr/bin/node
const process = require('process');
const request = require('request');
const requestURL = String(process.argv[2]);
let amount = 0;

request(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jsonBodyFilms = JSON.parse(body).results;
    const numberFilms = JSON.parse(body).count;
    for (let index = 0; index < numberFilms; index++) {
      if (jsonBodyFilms[index].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        amount = amount + 1;
      }
    }
    console.log(amount);
  }
});
