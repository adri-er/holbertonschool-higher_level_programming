$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: function (response) {
      $('#hello').append('<p>' + response.hello + '</p>');
    }
  });
});
