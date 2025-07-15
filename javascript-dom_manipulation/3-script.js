

toggleHeader = document.getElementById('toggle_header');

toggleHeader.addEventListener('click', function () {
    header = document.querySelector('header');
    if (header.classList.contains('red')) {
        header.classList.remove('red');
        header.classList.add('red');
    }
});
