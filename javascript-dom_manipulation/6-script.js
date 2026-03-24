fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    const nameElement = document.getElementById('character');
    nameElement.textContent = data.name;
  })
  .catch(error => console.error('Error fetching data:', error));
  