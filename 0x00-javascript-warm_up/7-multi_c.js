#!/usr/bin/node
const x = process.argv[2];
const string = 'C is fun';
let i = 0;

if (parseInt(x)) {
  while (i < x) {
    console.log(string);
    i++;
  }
} else {
  console.log('Missing number of ocurrences');
}
