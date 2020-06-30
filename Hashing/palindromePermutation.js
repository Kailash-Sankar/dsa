
// Check if any permutation of the input is a palindrome
function hasPalindromePermutation(theString) {

  const charSet = new Set();
  
  // track odd characters
  for (let c of theString) {
    charSet.has(c) ? charSet.delete(c) : charSet.add(c);
  }
  
  // for a palindrome, we'll either have
  // one odd char in the middle or no odd characters
  return charSet.size <= 1;
}
 

// first approach, using object
function _hasPalindromePermutation(theString) {

  const charList = theString.split('');
  const charMap = {};
  const charMod = {};
  
  charList.forEach( c => {
    charMap[c] = c in charMap ? charMap[c] + 1 : 1;
    charMod[c] = charMap[c] % 2;
  })
  
  const hasOddCount = Object.values(charMod).filter( x => x === 1);
  
  // for a palindrome, we'll either have
  // one odd char in the middle or no odd characters
  if (hasOddCount.length <= 1) {
      return true;
  }
  
  // we don't have to consider length of the string
  // one odd and rest even implies odd length
  return false;
}


// Tests

let desc = 'permutation with odd number of chars';
assertEqual(hasPalindromePermutation('aabcbcd'), true, desc);

desc = 'permutation with even number of chars';
assertEqual(hasPalindromePermutation('aabccbdd'), true, desc);

desc = 'no permutation with odd number of chars';
assertEqual(hasPalindromePermutation('aabcd'), false, desc);

desc = 'no permutation with even number of chars';
assertEqual(hasPalindromePermutation('aabbcd'), false, desc);

desc = 'empty string';
assertEqual(hasPalindromePermutation(''), true, desc);

desc = 'one character string ';
assertEqual(hasPalindromePermutation('a'), true, desc);

function assertEqual(a, b, desc) {
  if (a === b) {
    console.log(`${desc} ... PASS`);
  } else {
    console.log(`${desc} ... FAIL: ${a} != ${b}`);
  }
}
