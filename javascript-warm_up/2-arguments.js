#!/usr/bin/node


const { argv } = require('node:process');
const args = argv.slice(2);


if (argv.length === 0) {
    console.log("No argument");
} else if(argv.length === 1) {
    console.log("Argument found");
} else {
    console.log("arguments found");
}
