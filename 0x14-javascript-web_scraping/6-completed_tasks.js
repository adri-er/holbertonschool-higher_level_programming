#!/usr/bin/node
const process = require('process');
const request = require('request');
const requestURL = String(process.argv[2]);

request(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const listTodo = JSON.parse(body);
    const users = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0};
    for (let index = 0; index < listTodo.length; index++) {
      if (listTodo[index].completed === true) {
        users[listTodo[index].userId] += 1;
      }
    }
    for (let index = 0; index < 11; index++) {
      if (users[index + 1] === 0) {
        delete users[index + 1];
      }
    }
    console.log(users);
  }
});
