#!/usr/bin/node

const { argv } = require('node:process');

if (argv === 1) {
    console.log("No argument");
} else if(argv === 2) {
    console.log("Argument found");
} else {
    console.log("Arguments found");
}
