
async function listMovie() {
    const response = await fetch("https://swapi-api.hbtn.io/api/films/?format=json");
    const data = await response.json();
    const movies = data.results;
    const ul = document.getElementById("list_movies");

    movies.forEach(movie => {
        const li = document.createElement("li");
        li.textContent = movie.title;
        ul.appendChild(li);
    });
}
listMovie()
