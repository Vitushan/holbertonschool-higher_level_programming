#!/usr/bin/node

const x = Number(argv[2]);

if (!isNaN(x)) {
    console.log('Missing number of occurrences');
}else {
    console.log(x);
}
