#!/usr/bin/node

let n = 5, string = ""
    for (let i = 1; i < n; i++) {
    for (let j = 0; j < n; j++) {
        string += "*";
      }
      //break
      string += "\n";
    }
    console.log(string);
    