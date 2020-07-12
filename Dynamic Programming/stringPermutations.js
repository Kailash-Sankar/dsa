
// Generate all permutations of the input string
// recursively
function getPermutations(string) {

  // base for recursion
  if (string.length <= 1) {
    return new Set([string]);
  }

  // at each level find permutations of all characters except last
  const allCharsExceptLast = string.slice(0,-1);
  const lastChar = string[string.length - 1];
  
  const acelPermutations = getPermutations(allCharsExceptLast);
  
  const permutations = new Set();
  
  // add the last character in all possible positions
  // for each of the combinations of the first part
  acelPermutations.forEach( item => {
    // slice (0,0) is empty ''
    for(let position=0; position <= allCharsExceptLast.length; position++) {
      const sub = item.slice(0,position) + lastChar + item.slice(position);
      permutations.add(sub);
    }
    
  });

  return permutations;
}

// Tests

let desc = 'empty string';
let input = '';
let actual = getPermutations(input);
let expected = new Set(['']);
assert(isSetsEqual(actual, expected), desc);

desc = 'one character string';
input = 'a';
actual = getPermutations(input);
expected = new Set(['a']);
assert(isSetsEqual(actual, expected), desc);

desc = 'two character string';
input = 'ab';
actual = getPermutations(input);
expected = new Set(['ab', 'ba']);
assert(isSetsEqual(actual, expected), desc);

desc = 'three character string';
input = 'abc';
actual = getPermutations(input);
expected = new Set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']);
assert(isSetsEqual(actual, expected), desc);

function isSetsEqual(as, bs) {
  if (as.size !== bs.size) {
    return false;
  }
  for (let a of as) {
    if (!bs.has(a)) return false;
  }
  return true;
}

function assert(condition, desc) {
  if (condition) {
    console.log(`${desc} ... PASS`);
  } else {
    console.log(`${desc} ... FAIL`);
  }
}
