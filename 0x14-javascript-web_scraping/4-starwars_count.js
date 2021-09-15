#!/usr/bin/node
const process = require('process');
const request = require('request');
const requestURL = String(process.argv[2]);
let amount = 0;
const id = 18;

request(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jsonBodyFilms = JSON.parse(body).results;
    const numberFilms = JSON.parse(body).count;
    for (let index = 0; index < numberFilms; index++) {
      const linkList = jsonBodyFilms[index].characters;
      for (let indexJ = 0; indexJ < linkList.length; indexJ++) {
        if (linkList[indexJ].includes(String(id))) {
          amount = amount + 1;
          break;
        }
      }
    }
    console.log(amount);
  }
});
