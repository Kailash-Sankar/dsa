// given an array of integers
// Find a number that appears more than once
// there could be multiple duplicates, only need to find one.


// set approach
// O(n) time and O(n) space
function _findRepeat(numbers) {
  const items =  new Set();
  
  for(let i=0; i<numbers.length; i++) {
    if (items.has(numbers[i])) {
      return numbers[i];
    }
    items.add(numbers[i]);
  }

  throw 'no duplicate';
}


// space efficient approach
// O(nlogn) time and O(1) space
// applying binary search on the range of possible answers
// instead of the input array
function findRepeat(numbers) {
  
  // divide the range of numbers we are looking for
  // instead of dividing the input array
  let left = 1;
  let right = numbers.length-1;
  

  // left and right will converge on the duplicate number  
  while(left < right) {
    
    // divide our range in to two
    let mid = Math.floor((right+left) / 2);
    
    // count of expected numbers in the range
    let possibleDistinctCount = mid - left + 1;
    let actualCount = 0;
    
    // count the number of values in array
    // which match our range
    numbers.forEach( num => {
      if (num >= left && num <= mid) {
        actualCount++
      }
    })
    
    // if there's more, then the duplicate is in this range
    if (actualCount > possibleDistinctCount) {
      right = mid;
    }
    // otherwise it's in the upper range
    else {
      left = mid+1;
    }
  }
  
  return left;
}


// Tests

let desc = 'just the repeated number';
let actual = findRepeat([1, 1]);
let expected = 1;
assertEqual(actual, expected, desc);

desc = 'short array';
actual = findRepeat([1, 2, 3, 2]);
expected = 2;
assertEqual(actual, expected, desc);

desc = 'medium array';
actual = findRepeat([1, 2, 5, 5, 5, 5]);
expected = 5;
assertEqual(actual, expected, desc);

desc = 'long array';
actual = findRepeat([4, 1, 4, 8, 3, 2, 7, 6, 5]);
expected = 4;
assertEqual(actual, expected, desc);

function assertEqual(a, b, desc) {
  if (a === b) {
    console.log(`${desc} ... PASS`);
  } else {
    console.log(`${desc} ... FAIL: ${a} != ${b}`);
  }
}
