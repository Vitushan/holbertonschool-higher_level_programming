const new_btn = document.getElementById('update_header');

new_btn.addEventListener('click', function() {
    const header = document.querySelector('header');
    if (header) {
        header.textContent = "New Header ! ! ! "
    }
});
