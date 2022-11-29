#!/usr/bin/node
/**
 * Square class that inherits from previous square class
 */
const PrevSquare = require('./5-square');

class Square extends PrevSquare {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    const myChar = (c === undefined ? 'X' : c);
    for (let i = 0; i < this.size; i++) {
      let myVar = '';
      let y = 0;
      while (y < this.size) {
        myVar += myChar;
        y++;
      }

      console.log(myVar);
    }
  }
}

module.exports = Square;
