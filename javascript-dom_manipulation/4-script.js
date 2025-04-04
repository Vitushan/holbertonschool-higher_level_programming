const addItemButton = document.getElementById('add_item');
const myList = document.getElementsByClassName('my_list');

addItemButton.addEventListener('click', function() {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    myList[0].appendChild(newItem);
});
