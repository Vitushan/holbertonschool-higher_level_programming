#!/usr/bin/node

const { argv } = require('node:process');
if (argv === undefined) {
    console.log(argv[2] === 'No argument');
} else {
    console.log(argv[2]);
}
