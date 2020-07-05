 // in an ascending array of words 
 // a chuck from the starting was moved to the end of the array
 // Find the rotation point in the array

// burte approach
// iterate and find the first unordered point
function _findRotationPoint(words) {

  for(let i=1; i<words.length; i++) {
    if ( words[i-1] > words[i]) {
      return i;
    }
  }

  return false;
}

// a more efficient approach
// modified binary search
function findRotationPoint(words) {

  let leftIdx = 0;
  let rightIdx = words.length - 1;
  
  while(leftIdx <= rightIdx ) {
    
    // find middle index
    let midIdx = Math.floor((rightIdx + leftIdx)/2);
    
    // the the previous element is out of position
    // then this is the rotation point
    if ( midIdx-1 >= 0 && words[midIdx-1] > words[midIdx]) {
      return midIdx;
    }
    
    // if the first element is greater than mid
    // then the rotation point is to the left
    if ( words[0] > words[midIdx] ) {
      rightIdx =  midIdx - 1;
    }
    // if the first element is less than mid
    // then the rotation point is to the right
    else {
      leftIdx = midIdx + 1;
    }
    
  }
  
  return false;
}


// Tests

let desc = 'small array';
let actual = findRotationPoint(['cape', 'cake']);
let expected = 1;
assertEquals(actual, expected, desc);

desc = 'medium array';
actual = findRotationPoint(['grape', 'orange', 'plum', 'radish', 'apple']);
expected = 4;
assertEquals(actual, expected, desc);

desc = 'large array';
actual = findRotationPoint(['ptolemaic', 'retrograde', 'supplant',
  'undulate', 'xenoepist', 'asymptote',
  'babka', 'banoffee', 'engender',
  'karpatka', 'othellolagkage']);
expected = 5;
assertEquals(actual, expected, desc);

desc = 'invalid case, no rotation';
actual = findRotationPoint(['apple', 'grape', 'orange', 'plum', 'radish']);
expected = false;
assertEquals(actual, expected, desc);

function assertEquals(a, b, desc) {
  if (a === b) {
    console.log(`${desc} ... PASS`);
  } else {
    console.log(`${desc} ... FAIL: ${a} != ${b}`);
  }
}
