$('document').ready(function () {
  $('INPUT#btn_translate').click(function () {
    const langCode = $('INPUT#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });

  $('INPUT#language_code').keypress(function (e) {
    if (e.which === 13) {
      $('INPUT#btn_translate').click();
    }
  });
});
