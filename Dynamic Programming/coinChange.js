// Calculate the number of ways to make change

// bottom up approach
// starting from 0 to the amount, count no of possibilites for each demonination
// in asc order
function changePossibilities(amountLeft, denominations) {
  const ways = Array(amountLeft+1).fill(0);
  ways[0] = 1;
  
  denominations.forEach( d => {
    // for each demoniation, 
    // find the number of ways for each value from demoniation to the limit
    for(let amt = d; amt<= amountLeft; amt++) {
      const rem = amt-d;
      ways[amt] = ways[amt] + ways[rem];
    }
  });
  
  return ways[amountLeft];
}


// brute approach
const getKey = (items) => items.sort((a,b)=> a-b).join('-');

function diffChange(amountLeft, denominations, possibilities, applied=[]) {
  if (amountLeft === 0) { 
    possibilities.add(getKey(applied));
  }
  //console.log('->', amountLeft, count);
  
  for(let i=0; i<denominations.length; i++) {
    const d = denominations[i];
    if(d <= amountLeft) {
      diffChange(amountLeft-d, denominations, possibilities, [...applied, d]);
    }
  }

}

// Calculate the number of ways to make change
function changePossibilitiesBrute(amountLeft, denominations) {
  let possibilities = new Set();
  diffChange(amountLeft, denominations, possibilities);
  //console.log(possibilities);
  return possibilities.size;
}

// Tests
let desc = 'sample input';
let actual = changePossibilities(4, [1, 2, 3]);
let expected = 4;
assertEqual(actual, expected, desc);

desc = 'one way to make zero cents';
actual = changePossibilities(0, [1, 2]);
expected = 1;
assertEqual(actual, expected, desc);

desc = 'no ways if no coins';
actual = changePossibilities(1, []);
expected = 0;
assertEqual(actual, expected, desc);

desc = 'big coin value';
actual = changePossibilities(5, [25, 50]);
expected = 0;
assertEqual(actual, expected, desc);

desc = 'big target amount';
actual = changePossibilities(50, [5, 10]);
expected = 6;
assertEqual(actual, expected, desc);

desc = 'change for one dollar';
actual = changePossibilities(100, [1, 5, 10, 25, 50]);
expected = 292;
assertEqual(actual, expected, desc);

function assertEqual(a, b, desc) {
  if (a === b) {
    console.log(`${desc} ... PASS`);
  } else {
    console.log(`${desc} ... FAIL: ${a} != ${b}`)
  }
}
