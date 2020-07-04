// Determine if the tree is superbalanced
// depth between any two leaf nodes is at most one

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

// using BFS
function _isBalanced(treeRoot) {

  // maintain a queue for bread first search
  const bfsQ = [{ node: treeRoot, level: 0 }];
  // keep min and max levels
  let levelObj = { min: Infinity, max: 0 };
  
  
  while( bfsQ.length > 0) {
    const {node, level} = bfsQ.shift();
    
    // left node found
    // check and update min and max
    if(node.left === null && node.right === null) {
      if ( level < levelObj.min ) {
        levelObj.min = level;
      }
      else if ( level > levelObj.max) {
        levelObj.max = level;
      }
    }
    else {
      if(node.left) {
        bfsQ.push({ node: node.left, level: level + 1});
      }
    
      if(node.right) {
        bfsQ.push({ node: node.right, level: level + 1});
      }
    }
    
  }
  
  // check node depth diff
  if ( (levelObj.max - levelObj.min) <= 1) {
    return true;
  }

  return false;
}

// using DFS, short-circuit early
function isBalanced(treeRoot) {

  const dfsStack = [{ node: treeRoot, level: 0 }];
  // stack for depth first search
  let depths = [];
  
  
  while( dfsStack.length > 0) {
    const {node, level} = dfsStack.pop();
    
    // lead node found
    // if there are more than two unique depths
    // or if the diff between any two depths is greather than 1
    // then exit
    if(node.left === null && node.right === null) {
      if ( depths.indexOf(level) < 0) {
        depths.push(level);
        
        if (depths.length > 2 || (
          depths.length === 2 && Math.abs(depths[0] - depths[1]) > 1)) {
            return false;    
        }
      }
    }
    else {
      if(node.left) {
        dfsStack.push({ node: node.left, level: level + 1});
      }
    
      if(node.right) {
        dfsStack.push({ node: node.right, level: level + 1});
      }
    }
    
  }
  
  return true;
}


// Tests

let desc = 'full tree';
let treeRoot = new BinaryTreeNode(5);
let leftNode = treeRoot.insertLeft(8);
leftNode.insertLeft(1);
leftNode.insertRight(2);
let rightNode = treeRoot.insertRight(6);
rightNode.insertLeft(3);
rightNode.insertRight(4);
assertEquals(isBalanced(treeRoot), true, desc);

desc = 'both leaves at the same depth';
treeRoot = new BinaryTreeNode(3);
leftNode = treeRoot.insertLeft(4);
leftNode.insertLeft(1);
rightNode = treeRoot.insertRight(6);
rightNode.insertRight(9);
assertEquals(isBalanced(treeRoot), true, desc);

desc = 'leaf heights differ by one';
treeRoot = new BinaryTreeNode(6);
leftNode = treeRoot.insertLeft(1);
rightNode = treeRoot.insertRight(0);
rightNode.insertRight(7);
assertEquals(isBalanced(treeRoot), true, desc);

desc = 'leaf heights differ by two';
treeRoot = new BinaryTreeNode(6);
leftNode = treeRoot.insertLeft(1);
rightNode = treeRoot.insertRight(0);
rightNode.insertRight(7).insertRight(8);
assertEquals(isBalanced(treeRoot), false, desc);

desc = 'three leaves total';
treeRoot = new BinaryTreeNode(1);
leftNode = treeRoot.insertLeft(5);
rightNode = treeRoot.insertRight(9);
rightNode.insertLeft(8);
rightNode.insertRight(5);
assertEquals(isBalanced(treeRoot), true, desc);

desc = 'both subtrees superbalanced';
treeRoot = new BinaryTreeNode(1);
leftNode = treeRoot.insertLeft(5);
rightNode = treeRoot.insertRight(9);
rightNode.insertLeft(8).insertLeft(7);
rightNode.insertRight(5);
assertEquals(isBalanced(treeRoot), false, desc);

desc = 'both subtrees superbalanced two';
treeRoot = new BinaryTreeNode(1);
leftNode = treeRoot.insertLeft(2);
leftNode.insertLeft(3);
leftNode.insertRight(7).insertRight(8);
treeRoot.insertRight(4).insertRight(5).insertRight(6).insertRight(9);
assertEquals(isBalanced(treeRoot), false, desc);

desc = 'three leaves at different levels';
treeRoot = new BinaryTreeNode(1);
leftNode = treeRoot.insertLeft(2);
leftLeft = leftNode.insertLeft(3);
leftNode.insertRight(4);
leftLeft.insertLeft(5);
leftLeft.insertRight(6);
treeRoot.insertRight(7).insertRight(8).insertRight(9).insertRight(10);
assertEquals(isBalanced(treeRoot), false, desc);

desc = 'only one node';
treeRoot = new BinaryTreeNode(1);
assertEquals(isBalanced(treeRoot), true, desc);

desc = 'linked list tree';
treeRoot = new BinaryTreeNode(1);
treeRoot.insertRight(2).insertRight(3).insertRight(4);
assertEquals(isBalanced(treeRoot), true, desc);

function assertEquals(a, b, desc) {
  if (a === b) {
    console.log(`${desc} ... PASS`);
  } else {
    console.log(`${desc} ... FAIL: ${a} != ${b}`)
  }
}
