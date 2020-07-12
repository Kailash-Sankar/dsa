// Compute the nth Fibonacci number

// memoize calculate values
const fibMemo = {};

// recursive solution, exponential complexity
function _fib(n) {
  
  // invalid input
  if (n < 0 ) {
    throw new Error('Negative values are not allowed');
  }
  
  // base case
  if (n <= 1) {
    return n;
  }
  
  // return memoized value if available
  if (n in fibMemo) { return fibMemo[n]; }
  
  // calculate and memoize
  fibMemo[n-1] = fib(n-1);
  fibMemo[n-2] = fib(n-2);

  return fibMemo[n-1] + fibMemo[n-2];
}

// bottom up approach, O(n)
function fib(n) {
  
  // invalid input
  if (n < 0 ) {
    throw new Error('Negative values are not allowed');
  }
  
  // base case
  if (n <= 1) {
    return n;
  }
  
  prev = 0;
  current = 1;
  let next;
  
  for(let i=2; i<=n; i++) {
    next = current + prev;
    prev = current;
    current = next;
  }

  return next;
}


// Tests

let desc = 'zeroth fibonacci';
let actual = fib(0);
let expected = 0;
assertEqual(actual, expected, desc);

desc = 'first fibonacci';
actual = fib(1);
expected = 1;
assertEqual(actual, expected, desc);

desc = 'second fibonacci';
actual = fib(2);
expected = 1;
assertEqual(actual, expected, desc);

desc = 'third fibonacci';
actual = fib(3);
expected = 2;
assertEqual(actual, expected, desc);

desc = 'fifth fibonacci';
actual = fib(5);
expected = 5;
assertEqual(actual, expected, desc);

desc = 'tenth fibonacci';
actual = fib(10);
expected = 55;
assertEqual(actual, expected, desc);

desc = 'negative fibonacci';
const negativeFib = () => (fib(-1));
assertThrowsError(negativeFib, desc);

function assertEqual(a, b, desc) {
  if (a === b) {
    console.log(`${desc} ... PASS`);
  } else {
    console.log(`${desc} ... FAIL: ${a} != ${b}`)
  }
}

function assertThrowsError(func, desc) {
  try {
    func();
    console.log(`${desc} ... FAIL`);
  } catch (e) {
    console.log(`${desc} ... PASS`);
  }
}
