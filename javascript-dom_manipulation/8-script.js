window.addEventListener('DOMContentLoaded', function () {
  const helloDiv = document.getElementById('hello');

  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => {
      helloDiv.textContent = data.hello;
    })
    .catch(error => {
      console.error('Error fetching hello:', error);
      helloDiv.textContent = 'Failed to load greeting.';
    });
});
