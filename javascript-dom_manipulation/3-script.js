const toggleHeader = document.querySelector('#toggle_header');
const header = document.querySelector('header');

toggleHeader.addEventListener('click', () => {
  header.className = header.classList.contains('red') ? 'green' : 'red';
});
