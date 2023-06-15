#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('This is not a  number');
} else {
  console.log('My Number:', parseInt(process.argv[2]));
}
