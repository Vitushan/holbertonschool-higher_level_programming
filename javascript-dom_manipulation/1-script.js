 const elementClick = document.getElementById('red_header');

 elementClick.addEventListener('click', function() {
    const myH1 = document.querySelector('h1');
    if (myH1) {
        myH1.style.color = '#FF0000'
    }
 });