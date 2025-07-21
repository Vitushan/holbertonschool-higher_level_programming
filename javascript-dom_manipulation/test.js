#!/usr/bin/node
document.addEventListener('DOMContentLoaded', async () => {
  const urlFetch = await fetch('https://hellosalut.stefanbohacek.dev/?lang=fr');
  const urlJson = await urlFetch.json();
  const hello = document.querySelector('#hello');
  hello.textContent = urlJson.hello;
});