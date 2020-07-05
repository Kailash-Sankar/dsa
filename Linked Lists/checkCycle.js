// check if the linked list contains a cycle

class LinkedListNode {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

// set approach
// O(n) time and O(n) space
function _containsCycle(firstNode) {
  
  let node = firstNode;
  const visited = new Set();
  
  while(node) {
    // check if this node was visited before
    if (visited.has(node)) {
      return true;
    }
    
    visited.add(node);
    node = node.next;
  }
  
  return false;
}

// runner approach
// O(n) time and O(1) space
function containsCycle(firstNode) {
  
  // slow runner will move one node at a time
  // fast runner will move two nodes at a time
  let slowRunner = firstNode;
  let fastRunner = firstNode;
  
  while( fastRunner && fastRunner.next) {
    
    slowRunner = slowRunner.next;
    fastRunner = fastRunner.next.next;
    
    // slow and fast runner will overlap if there's a cycle
    if (slowRunner === fastRunner) {
      return true;
    }
    
  }
  
  return false;
}


// Tests

let desc = 'linked list with no cycle';
let nodes = valuesToLinkedListNodes([1, 2, 3, 4]);
assertEquals(containsCycle(nodes[0]), false, desc);

desc = 'cycle loops to beginning';
nodes = valuesToLinkedListNodes([1, 2, 3, 4]);
nodes[3].next = nodes[0];
assertEquals(containsCycle(nodes[0]), true, desc);

desc = 'cycle loops to middle';
nodes = valuesToLinkedListNodes([1, 2, 3, 4, 5]);
nodes[4].next = nodes[2];
assertEquals(containsCycle(nodes[0]), true, desc);

desc = 'two node cycle at end';
nodes = valuesToLinkedListNodes([1, 2, 3, 4, 5]);
nodes[4].next = nodes[3];
assertEquals(containsCycle(nodes[0]), true, desc);

desc = 'empty list';
assertEquals(containsCycle(null), false, desc);

desc = 'one element linked list no cycle';
let firstNode = new LinkedListNode(1);
assertEquals(containsCycle(firstNode), false, desc);

desc = 'one element linked list cycle';
firstNode = new LinkedListNode(1);
firstNode.next = firstNode;
assertEquals(containsCycle(firstNode), true, desc);

function valuesToLinkedListNodes(values) {
  const nodes = [];
  for (let i = 0; i < values.length; i++) {
    const node = new LinkedListNode(values[i]);
    if (i > 0) {
      nodes[i - 1].next = node;
    }
    nodes.push(node);
  }
  return nodes;
}

function assertEquals(a, b, desc) {
  if (a === b) {
    console.log(`${desc} ... PASS`);
  } else {
    console.log(`${desc} ... FAIL: ${a} != ${b}`);
  }
}
