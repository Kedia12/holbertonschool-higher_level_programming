const item = document.getElementById('add_item');

item.addEventListener('click', () => {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  document.querySelector('.my_list').appendChild(newItem);
});
