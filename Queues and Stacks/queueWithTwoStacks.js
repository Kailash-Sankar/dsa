// Implement a queue with two stacks

// basic stack implementation
class Stack {
  constructor() {
    // Initialize an empty stack
    this.items = [];
  }

  // Push a new item onto the stack
  push(item) {
    this.items.push(item);
  }

  // Remove and return the last item
  pop() {
    // If the stack is empty, return null
    // (It would also be reasonable to throw an exception)
    if (!this.items.length) {
      return null;
    }
    return this.items.pop();
  }

  // Return the last item without removing it
  peek() {
    if (!this.items.length) {
      return null;
    }
    return this.items[this.items.length - 1];
  }
}

//  Implement the enqueue and dequeue methods
class QueueTwoStacks {
  constructor() {
    this.intStk = new Stack();
    this.extStk =  new Stack();
  }
  
  enqueue(item) {
    this.intStk.push(item);
  }

  dequeue() {
    // if external stack is empty, move items to it
    if( this.extStk.peek() === null) {
      this.switchOver();
    }
    
    const item = this.extStk.pop();
    // still empty? then throw exception
    if ( item === null ) { throw('Queue is empty'); }
    return item;
  }
  
  // move from internal stack to external stack
  // generates queue FIFO structure for all current items in int stack
  switchOver() {
    while(this.intStk.peek() !== null) {
      this.extStk.push(this.intStk.pop());
    }
  }
}

// Tests
const q = new QueueTwoStacks();

q.enqueue(1);
q.enqueue(2);
q.enqueue(3);

let desc = 'dequeue #1';
let actual = q.dequeue();
let expected = 1;
assertEquals(actual, expected, desc);

desc = 'dequeue #2';
actual = q.dequeue();
expected = 2;
assertEquals(actual, expected, desc);

q.enqueue(4);

desc = 'dequeue #3';
actual = q.dequeue();
expected = 3;
assertEquals(actual, expected, desc);

desc = 'dequeue #4';
actual = q.dequeue();
expected = 4;
assertEquals(actual, expected, desc);

desc = 'dequeue from empty queue';
const emptyDequeue = () => q.dequeue();
assertThrowsError(emptyDequeue, desc);

function assertEquals(a, b, desc) {
  if (a === b) {
    console.log(`${desc} ... PASS`);
  } else {
    console.log(`${desc} ... FAIL: ${a} != ${b}`);
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
