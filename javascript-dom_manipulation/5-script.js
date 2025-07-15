const btn = document.getElementById('update_header');

btn.addEventListener('click', function() {
    const header = document.querySelector('header');
    if (header) {
        header.textContent = "News Header ! ! ! "
    }
});