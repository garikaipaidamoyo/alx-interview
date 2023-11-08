#!/usr/bin/node
const axios = require('axios');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a Movie ID as the first argument.');
  process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieId}/`;

axios.get(url)
  .then(response => {
    const film = response.data;
    const characters = film.characters;

    const fetchCharacter = async (characterUrl) => {
      try {
        const characterResponse = await axios.get(characterUrl);
        const character = characterResponse.data;
        console.log(character.name);
      } catch (error) {
        console.error('Error fetching character:', error);
      }
    };

    const fetchAllCharacters = async () => {
      for (const characterUrl of characters) {
        await fetchCharacter(characterUrl);
      }
    };

    fetchAllCharacters();
  })
  .catch(error => {
    console.error('Error:', error);
  });
