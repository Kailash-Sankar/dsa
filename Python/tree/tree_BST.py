# binary search tree
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

    # in order traversal
    def _inorder(self,node):
        if node:
            self._inorder(node.left)
            self.sorted.append(node.val)
            self._inorder(node.right)

    # find height of a tree
    def height(self):
        return self._findHeight(self.root)        
        
    def _findHeight(self,node):
        if node is None:
            return -1;
        l = self._findHeight(node.left)
        r = self._findHeight(node.right)
        return max(l,r) + 1;

    # level order traversal
    def levels(self):
        if self.root is None:
            Print('Tree is empty')
        else:
            self._q = [self.root];
            while len(self._q) > 0:
                node = self._q.pop(0);
                if node:
                    print(node.val)
                    self._q.append(node.left);
                    self._q.append(node.right);
    # level order traversal with level information
    def lro(self):
        if self.root is None:
            print('empty')
        else:
            self._q = [self.root,'-'];
            self._lvl = 1
            while len(self._q) > 0:
                #print('queue',self._q)
                node = self._q.pop(0)

                if node == '-':
                    if len(self._q) == 0:
                        break;
                    print('-' * self._lvl)
                    self._lvl += 1;
                    self._q.append('-')
                else:
                    print(node.val,end=' ')
                    if node.left is not None:
                        self._q.append(node.left)
                    if node.right is not None:
                        self._q.append(node.right)
            print();
     
                
              
bst = BST();
for i in range(10):
    val = randint(1,100)
    print(val,end=' ')
    bst.add(val)
print();
print(bst)
print('Height of BST',bst.height());
print('-----');
bst.levels();
print('-----');
bst.lro();