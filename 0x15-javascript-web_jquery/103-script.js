#!/usr/bin/node
$(function () {
  $('#btn_translate').click(function () {
    const code = $('#language_code').val();
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + code, function (data) {
      $('#hello').text(data.hello);
    });
  });
  $('#language_code').focus(function () {
    $('#language_code').keyup(function (e) {
      if (e.which === 13) { // 13 for 'enter' key
        const code = $('#language_code').val();
        $.get('https://hellosalut.stefanbohacek.dev/?lang=' + code, function (data) {
          $('#hello').text(data.hello);
        });
      }
    });
  });
});
