document.addEventListener('DOMContentLoaded', function () {
  const listMovies = document.getElementById('list_movies');

  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
      const movies = data.results;
      movies.forEach(movie => {
        const li = document.createElement('li');
        li.textContent = movie.title;
        listMovies.appendChild(li);
      });
    })
    .catch(error => {
      console.error('Error fetching movies:', error);
      listMovies.textContent = 'Failed to load movies.';
    });
});
