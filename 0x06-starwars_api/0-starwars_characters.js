#!/usr/bin/node
/**
 * script that prints all characters of a Star Wars movie:
 * The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
 * Display one character name per line in the same order as the “characters” list in the /films/ endpoint
 * You must use the Star wars API
 * You must use the request module
 */
const request = require('request');
const api = 'https://swapi-api.alx-tools.com/api/films/';
const movieID = process.argv[2];

request(api + movieID, (err, res, body) => {
  if (err) console.error(err);
  if (res.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    displayCharacter(characters, 0);
  } else {
    console.log(`Error code: ${res.statusCode}`);
  }
});

const displayCharacter = (characterArr, index) => {
  request.get(characterArr[index], (error, resp, body) => {
    if (error) console.error(error);
    console.log(JSON.parse(body).name);
    if (index + 1 < characterArr.length) {
      displayCharacter(characterArr, index + 1);
    }
  });
};
