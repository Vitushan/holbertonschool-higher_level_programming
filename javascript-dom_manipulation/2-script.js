const redHeader = document.getElementById('red_header')

redHeader.addEventListener('click', function() {
    const header = document.querySelector('h1');
    if (header) {
        header.classList.add('red');
    }   
});