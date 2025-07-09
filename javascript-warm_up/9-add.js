#!/usr/bin/node

function add(a, b) {
    return a + b
}

const { argv } = require('node:process');

const a = argv[2];
const b = argv[3];
console.log(add(a, b));
