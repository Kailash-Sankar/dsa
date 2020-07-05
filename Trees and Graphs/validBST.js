// check if a binary tree is a valid
// binary search tree

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

// recursively build sorted array
// inorder travel, ascending
function _inorder(node, arr) {
  if (!node) {
    return true;
  }
  
  // check left node
  let l = inorder(node.left, arr);
  
  // check for out of order value
  if ( arr.length > 0 && arr[arr.length - 1] > node.value) {
    return false;
  }
  // push current node value
  arr.push(node.value);
  
  // check right node
  let r = inorder(node.right, arr);
  
  return l && r;
}

// a more space efficient approach
// instead of an array of nodes, just keep the last element
// still an array, as it has to be passed as reference
function inorder(node, arr) {
  if (!node) {
    return true;
  }
  
  // check left node
  let l = inorder(node.left, arr);
  
  // check for out of order value
  if ( arr[0] && arr[0] >= node.value) {
    return false;
  }
  // push current node value
  arr[0] = node.value
  
  // check right node
  let r = inorder(node.right, arr);
  
  return l && r;
}

// Determine if the tree is a valid binary search tree
function isBinarySearchTree(treeRoot) {
  const arr = [null];
  return inorder(treeRoot, arr);
}



// Tests

let desc = 'valid full tree';
let treeRoot = new BinaryTreeNode(50);
let leftNode = treeRoot.insertLeft(30);
leftNode.insertLeft(10);
leftNode.insertRight(40);
let rightNode = treeRoot.insertRight(70);
rightNode.insertLeft(60);
rightNode.insertRight(80);
assertEquals(isBinarySearchTree(treeRoot), true, desc);

desc = 'both subtrees valid';
treeRoot = new BinaryTreeNode(50);
leftNode = treeRoot.insertLeft(30);
leftNode.insertLeft(20);
leftNode.insertRight(60);
rightNode = treeRoot.insertRight(80);
rightNode.insertLeft(70);
rightNode.insertRight(90);
assertEquals(isBinarySearchTree(treeRoot), false, desc);

desc = 'descending linked list';
treeRoot = new BinaryTreeNode(50);
leftNode = treeRoot.insertLeft(40);
leftNode = leftNode.insertLeft(30);
leftNode = leftNode.insertLeft(20);
leftNode = leftNode.insertLeft(10);
assertEquals(isBinarySearchTree(treeRoot), true, desc);

desc = 'out of order linked list';
treeRoot = new BinaryTreeNode(50);
rightNode = treeRoot.insertRight(70);
rightNode = rightNode.insertRight(60);
rightNode = rightNode.insertRight(80);
assertEquals(isBinarySearchTree(treeRoot), false, desc);

desc = 'one node tree';
treeRoot = new BinaryTreeNode(50);
assertEquals(isBinarySearchTree(treeRoot), true, desc);

function assertEquals(a, b, desc) {
  if (a === b) {
    console.log(`${desc} ... PASS`);
  } else {
    console.log(`${desc} ... FAIL: ${a} != ${b}`)
  }
}
