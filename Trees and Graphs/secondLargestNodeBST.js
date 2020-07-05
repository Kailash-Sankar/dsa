// find the second largest node in a BST

class BinaryTreeNode {
  constructor(value) {
    this.value = value;
    this.left  = null;
    this.right = null;
  }

  insertLeft(value) {
    this.left = new BinaryTreeNode(value);
    return this.left;
  }

  insertRight(value) {
    this.right = new BinaryTreeNode(value);
    return this.right;
  }
}

// recursive dfs approach
// build descending order of elements
// stop at 2
function dfs(node, arr) {
  if (node) {
    dfs(node.right, arr);
    if (arr.length < 2) {
      arr.push(node.value);
    }
    dfs(node.left, arr);
  }
}

// Find the second largest item in the binary search tree
function _findSecondLargest(treeRoot) {
  const arr = [];
  dfs(treeRoot, arr);
  if(arr.length < 2) {  throw 'Second largest element is not available'; }

  return arr.pop();
}

// non recursive approach
// reduces space complexity (stack overflow of recursion)
function findLargest(node) {
  let current = node;
  while (current) {
    if (!current.right) {
      return current.value;
    }
    current = current.value;
  }
}

// iterate till the right most element is found
function findSecondLargest(treeRoot) {
  
  if(!treeRoot || (!treeRoot.left && !treeRoot.right)) {
    throw new Error('Second largest element is not available');
  }
  
  let current = treeRoot;
  while (current) {
    
    // right most node with a left subtree
    // second largest element will be in the left subtree
    if (current.left && !current.right) {
      return findLargest(current.left);
    }
    
    // right most node without a left subtree
    // parent(current) node is the second largest element
    if ( current.right
      && !current.right.left
      && !current.right.right) {
        return current.value
    }
    
    current = current.right;
  }
}


// Tests

let desc = 'full tree';
let treeRoot = new BinaryTreeNode(50);
let leftNode = treeRoot.insertLeft(30);
leftNode.insertLeft(10);
leftNode.insertRight(40);
let rightNode = treeRoot.insertRight(70);
rightNode.insertLeft(60);
rightNode.insertRight(80);
assertEquals(findSecondLargest(treeRoot), 70, desc);

desc = 'largest has a left child';
treeRoot = new BinaryTreeNode(50);
leftNode = treeRoot.insertLeft(30);
leftNode.insertLeft(10);
leftNode.insertRight(40);
rightNode = treeRoot.insertRight(70);
rightNode.insertLeft(60);
assertEquals(findSecondLargest(treeRoot), 60, desc);

desc = 'largest has a left subtree';
treeRoot = new BinaryTreeNode(50);
leftNode = treeRoot.insertLeft(30);
leftNode.insertLeft(10);
leftNode.insertRight(40);
rightNode = treeRoot.insertRight(70);
leftNode = rightNode.insertLeft(60);
leftNode.insertRight(65);
leftNode = leftNode.insertLeft(55);
leftNode.insertRight(58);
assertEquals(findSecondLargest(treeRoot), 65, desc);

desc = 'second largest is root node';
treeRoot = new BinaryTreeNode(50);
leftNode = treeRoot.insertLeft(30);
leftNode.insertLeft(10);
leftNode.insertRight(40);
rightNode = treeRoot.insertRight(70);
assertEquals(findSecondLargest(treeRoot), 50, desc);

desc = 'descending linked list';
treeRoot = new BinaryTreeNode(50);
leftNode = treeRoot.insertLeft(40);
leftNode = leftNode.insertLeft(30);
leftNode = leftNode.insertLeft(20);
leftNode = leftNode.insertLeft(10);
assertEquals(findSecondLargest(treeRoot), 40, desc);

desc = 'ascending linked list';
treeRoot = new BinaryTreeNode(50);
rightNode = treeRoot.insertRight(60);
rightNode = rightNode.insertRight(70);
rightNode = rightNode.insertRight(80);
assertEquals(findSecondLargest(treeRoot), 70, desc);

desc = 'one node tree';
treeRoot = new BinaryTreeNode(50);
assertThrowsError(() => findSecondLargest(treeRoot), desc);

desc = 'when tree is empty';
treeRoot = null;
assertThrowsError(() => findSecondLargest(treeRoot), desc);

function assertEquals(a, b, desc) {
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
