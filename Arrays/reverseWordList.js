
  // reverse words from an array of characters
  // words are separated by space
  
// util for reversal
function reverse(message, startIdx, endIdx) {
  // swap left and right, meet in the middle
  while(startIdx < endIdx) {
    let temp = message[startIdx];
    message[startIdx] = message[endIdx];
    message[endIdx] = temp;
    startIdx++;
    endIdx--;
  }
}

// an optimal appraoch
function reverseWords(message) {
  
  // reverse entire message
  reverse(message, 0, message.length-1);
  
  // re-reverse individual words ony by one
  let startIdx = 0;
  for(let i=0;i<= message.length;i++) {
    if ( i === message.length || message[i] === ' ') {
      reverse(message, startIdx, i-1);
      startIdx=i+1;
    }
  }
}
  
// a brute appraoch 
function reverseWordsBrute(message) {

  // find start and end index of all words
  const breakIndices = [];
  let start = 0;
  for(let i=0;i<message.length;i++) {
    if (message[i] === ' ') {
      breakIndices.push([start,i]);
      start = i+1;
    }
  }
  breakIndices.push([start,message.length]);
  
  // swap left and right, meet in the middle
  let diff = 0;
  for(let x=0,y=breakIndices.length-1; x<y; x++,y--) {
    
    // each time we slice, the indexes change
    // add diff to get the new word start/end indexes
    let bx = breakIndices[x].map( f => f + diff);
    let by = breakIndices[y].map( g => g + diff);
    
    // the left and right words for swapping
    let leftSect = message.slice(...bx);
    let rightSect = message.slice(...by);
    
    // the difference to add to account for "scoot over"
    sizeDiff  = rightSect.length - leftSect.length;
    
    // splice and swap
    message.splice(bx[0], leftSect.length, ...rightSect);
    // size diff is addded to account for index position change
    message.splice(by[0] + sizeDiff, rightSect.length, ...leftSect);
    
    // update our index shift difference
    diff = diff + sizeDiff;
  }
  
}


// Tests

let desc = 'one word';
let input = 'vault'.split('');
reverseWords(input);
let actual = input.join('');
let expected = 'vault';
assertEqual(actual, expected, desc);

desc = 'two words';
input = 'thief cake'.split('');
reverseWords(input);
actual = input.join('');
expected = 'cake thief';
assertEqual(actual, expected, desc);

desc = 'three words';
input = 'one another get'.split('');
reverseWords(input);
actual = input.join('');
expected = 'get another one';
assertEqual(actual, expected, desc);

desc = 'multiple words same length';
input = 'rat the ate cat the'.split('');
reverseWords(input);
actual = input.join('');
expected = 'the cat ate the rat';
assertEqual(actual, expected, desc);

desc = 'multiple words different lengths';
input = 'yummy is cake bundt chocolate'.split('');
reverseWords(input);
actual = input.join('');
expected = 'chocolate bundt cake is yummy';
assertEqual(actual, expected, desc);

desc = 'empty string';
input = ''.split('');
reverseWords(input);
actual = input.join('');
expected = '';
assertEqual(actual, expected, desc);

function assertEqual(a, b, desc) {
  if (a === b) {
    console.log(`${desc} ... PASS`);
  } else {
    console.log(`${desc} ... FAIL: ${a} != ${b}`);
  }
}
