#!/usr/bin/node
const arrayValues = process.argv;
const organizedArray = [];
for (let i = 2; i < arrayValues.length; i++) {
  organizedArray[i - 2] = parseInt(arrayValues[i]);
}
if (arrayValues.length < 4) {
  console.log(0);
} else {
  organizedArray.sort();
  organizedArray.reverse();
  console.log(organizedArray[1]);
}
