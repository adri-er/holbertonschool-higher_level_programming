#!/usr/bin/node
if (typeof process.argv[2] !== 'undefined') {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
