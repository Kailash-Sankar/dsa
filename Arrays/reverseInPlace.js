 // reverse an array of characters in palce
 
 // arrayOfChars.reverse() works
 // this solution is generic to all languages
 function reverse(arrayOfChars) {

  // swap left and right, meet in the middle
  for(let i=0, j=arrayOfChars.length-1; i<j; i++,j--) {
    let temp = arrayOfChars[i];
    arrayOfChars[i] = arrayOfChars[j];
    arrayOfChars[j] = temp;
  }  
}
