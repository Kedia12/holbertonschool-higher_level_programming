#!/usr/bin/node
const argv1 = process.argv[2];
if (parseInt(argv1)) {
  console.log('My number: ' + parseInt(argv1));
} else {
  console.log('Not a number');
}
