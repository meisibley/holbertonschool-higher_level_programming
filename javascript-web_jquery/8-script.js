#!/usr/bin/node
// Write a JavaScript script that fetches and lists the title for all movies
// by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
$.get('https://swapi-api.hbtn.io/api/films/?format=json', data =>
  data.results.forEach(film =>
    $('UL#list_movies').append(`<li>${film.title}</li>`)));
