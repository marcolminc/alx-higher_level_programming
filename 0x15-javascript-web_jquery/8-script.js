#!/usr/bin/node
$(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    $.each(data.results, function (i, v) {
      const li = $('<li></li>').text(v.title);
      $('#list_movies').append(li);
    });
  });
});
