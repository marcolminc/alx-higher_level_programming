#!/usr/bin/node
$(function () {
  $('#add_item').click(function () {
    const li = $('<li></li>').text('Item');
    $('ul.my_list').append(li);
  });
});
