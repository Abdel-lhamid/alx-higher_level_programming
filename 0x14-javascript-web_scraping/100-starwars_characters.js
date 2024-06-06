#!/usr/bin/node

const req = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
req.get(url + id, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const characters = data.characters;
  for (const c of characters) {
    req.get(c, function (error, res, body1) {
      if (error) {
        console.log(error);
      }
      const chardata = JSON.parse(body1);
      console.log(chardata.name);
    });
  }
});
