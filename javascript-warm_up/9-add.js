#!/usr/bin/node

function add(a, b) {
    return a + b
}
const { argv } = require('node:process');
const a = Number(argv[2]);
const b = Number(argv[3]);
console.log(add(a, b));
