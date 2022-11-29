#!/usr/bin/node
/**
 * Check the parameters provided
 */
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let myVar = '';
      const y = 0;
      while (y < this.width) {
        myVar += 'X';
      }

      console.log(myVar);
    }
  }
}
module.exports = Rectangle;
