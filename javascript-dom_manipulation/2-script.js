

redHeader = document.getElementById('red_header')

redHeader.addEventListener('click', function() {
    header = document.querySelector('h1');
    if (header) {
        header.classList.add('red');
    }   
});
