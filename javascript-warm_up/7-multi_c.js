#!/usr/bin/node

const { argv } = require('node:process')
const x = Number(argv[2]);

if (isNaN(x)) {
    console.log('Missing number of occurrences');
}else {
    console.log(x);
}
