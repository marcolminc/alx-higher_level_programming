#!/usr/bin/node
$(function () {
  $('#toggle_header').click(function () {
    $('header').toggleClass('red').toggleClass('green');
  });
});
