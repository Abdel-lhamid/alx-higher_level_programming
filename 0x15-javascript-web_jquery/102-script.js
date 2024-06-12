$('document').ready(function () {
  $('#btn_translate').click(function () {
    $.get('https://fourtonfish.com/hellosalut/?lang=' + $('#language_code').val(), function (data) {
      $('#hello').text(data.hello);
    });
  });
});
