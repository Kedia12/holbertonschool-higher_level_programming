#!/usr/bin/node
const myVar = 'C is fun';
const n = process.argv[2];
if (isNaN(n)) {
  console.log('Missing number of occurrences');
} else {
  parseInt(n);
  for (let i = 0; i < n; i++) {
    console.log(myVar);
  }
}
