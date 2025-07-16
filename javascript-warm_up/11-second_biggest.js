#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length < 2) {
  console.log(0);
} else {
  // arrange the numbers in descending order
  const sorted = args.sort((a, b) => b - a);

  // take second biggest number
  let secondBiggest = sorted[1];
  // If the second largest number is equal to the first (meaning the numbers are repeated), we must look for a different second number.

  for (let i = 1; i < sorted.length; i++) {
    if (sorted[i] < sorted[0]) {
      secondBiggest = sorted[i];
      break;
    }
  }
  console.log(secondBiggest);
}
