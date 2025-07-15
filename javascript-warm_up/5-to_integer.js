#!/usr/bin/node

const input = process.argv[2];
const number = Number(input);

if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
