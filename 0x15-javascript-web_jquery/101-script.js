#!/usr/bin/node
$(function () {
  $('#add_item').click(function () {
    const li = $('<li></li>').text('Item');
    $('ul.my_list').append(li);
  });

  $('#remove_item').click(function () {
    $('ul.my_list li:last-child').remove();
  });

  $('#clear_list').click(function () {
    $('ul.my_list li').remove();
  });
});
