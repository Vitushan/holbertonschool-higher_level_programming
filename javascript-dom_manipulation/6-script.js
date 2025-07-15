
async function displayName() {
  const response = await fetch("https://swapi-api.hbtn.io/api/people/5/?format=json");
  const character = await response.json();
  document.getElementById("character").textContent = character.name;
}

displayName();
