
myList = document.getElementById('add_item');
myList.addEventListener('click', function() {
    list = document.querySelector('.my_list');
    new_item = document.createElement('li');
    new_item.textContent = "Item";
    list.appendChild(new_item);
});