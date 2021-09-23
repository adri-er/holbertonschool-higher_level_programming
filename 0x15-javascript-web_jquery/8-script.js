$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: function (response) {
      $.each(response.results, function (i, item) {
        $('UL#list_movies').append('<li>' + item.title + '</li>');
      });
    }
  });
});
