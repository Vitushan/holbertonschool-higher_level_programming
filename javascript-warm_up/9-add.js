#!/usr/bin/node

const { argv } = require('node:process');
const a = Number(argv[2]);
const b = Number(argv[3]);

function add(a, b) {
    return a + b
}
console.log(add(a, b));
