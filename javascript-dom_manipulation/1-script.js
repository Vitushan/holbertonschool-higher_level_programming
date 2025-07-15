
element = document.querySelector('h1');
element.style.color = "#FF0000";

elementClick = document.getElementById('red_header');

 elementClick.addEventListener('click', function() {
    myH1 = document.querySelector('h1');
    if (myH1) {
        myH1.style.color = '#FF0000'
    }
 });
