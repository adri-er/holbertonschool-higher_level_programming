#!/usr/bin/node
function callMeMoby (x, theFunction) {
  while (x > 0) {
    theFunction();
    x--;
  }
}
module.exports.callMeMoby = callMeMoby;
