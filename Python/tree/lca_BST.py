# binary search tree
# lowest common ancestor
from random import randint;

class Node:
    def __init__(self,val):
        self.val = val;
        self.right = None;
        self.left = None;

    def __repr__(self):
        return str(self.val);

class BST():
    def __init__(self):
        self.root = None;

    def add(self,val):
        if self.root is None:
            self.root = Node(val);
        else:
            self._add(self.root,val)

    def _add(self,node,val):
        if val <= node.val:
            if node.left:
                self._add(node.left,val)
            else:
                node.left = Node(val)
        else:
            if node.right:
                self._add(node.right,val)
            else:
                node.right = Node(val)

    def __repr__(self):
        if self.root is None:
            print('Tree is empty :(')
        else:
            self.sorted = [];
            self._inorder(self.root)
            return str(self.sorted)

    def _inorder(self,node):
        if node:
            self._inorder(node.left)
            self.sorted.append(node.val)
            self._inorder(node.right)

    # find the lowest common ancestor
    # assumes inputs a and b are in the tree
    def lcs(self,a,b):
        if self.root is None:
            print('Tree is empty')
            return

        found = 0
        node = self.root
        while not found:
            if a < node.val and b < node.val:
                node = node.left
            elif a > node.val and b > node.val:
                node = node.right
            else:
                found = 1

        print('LCS',node)

    # vertical slicing
    def vro(self):
        if self.root is None:
            print('empty')
        else:
            self._v = {}
            self._vertical(self.root,0)
        print('verticals',self._v)

    def _vertical(self,node,vline):
        if vline in self._v:
            self._v[vline].append(node.val)
        else:
            self._v[vline] = [node.val];

        if node.left is not None:
            self._vertical(node.left,vline-1)

        if node.right is not None:
            self._vertical(node.right,vline+1)

bst = BST();
#for i in range(10):
#    val = randint(1,100)
#    print(val,end=' ')
#    bst.add(val)

test_case_1 = [28,48,62,93,3,76,35,69,16,88]
print("Test Case 1",test_case_1)
for j in test_case_1:
    bst.add(j);
print(bst)
bst.vro();
print("-----------------------");

# output - 62
bst.lcs(62,69);

# output - 48
bst.lcs(38,88)

# output - 28
bst.lcs(16,62)
