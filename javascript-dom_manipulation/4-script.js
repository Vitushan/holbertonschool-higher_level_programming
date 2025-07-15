
const myList = document.getElementById('add_item');
myList.addEventListener('click', function() {
    const list = document.querySelector('.my_list');
    const new_item = document.createElement('li');
    new_item.textContent = "Item";
    list.appendChild(new_item);
});