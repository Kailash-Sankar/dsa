class Node:
    def __init__(self,val):
        self.val = val
        self.left =  None
        self.right = None

class BT:
    def __init__(self):
        self.root = None
        
    def isequal(self,tree):
        e = self._iseq(self.root,tree.root)
        if e:
            print("Tree's are erqual")
        else:
            print("Nope. Not equal")            
        
    def _iseq(self,n,m):        
        if n is None and m is None:
            return 1;
        elif n is None or m is None:
            return 0
        
        if n.val == m.val:            
            return self._iseq(n.left,m.left) and self._iseq(n.right,m.right)
        else:
            return 0
        
def test():
    print('--- test case 1 ---')
    bt1 = BT();
    bt1.root = Node(1);
    bt1.root.left = Node(2)
    bt1.root.right = Node(3)
    bt1.root.left.left = Node(4)
    bt1.root.left.right = Node(5)
    bt1.root.right.left = Node(6)
    bt1.root.right.right = Node(7)
    
    bt2 = BT();
    bt2.root = Node(1);
    bt2.root.left = Node(2)
    bt2.root.right = Node(3)
    bt2.root.left.left = Node(4)
    bt2.root.left.right = Node(5)
    bt2.root.right.left = Node(6)
    bt2.root.right.right = Node(7)
       
    bt1.isequal(bt2)
    
    print('--- test case 2 ---')
    bt3 = BT();
    bt3.root = Node(1);
    bt3.root.left = Node(2)
    bt3.root.right = Node(3)
    bt3.root.left.left = Node(4)
    bt3.root.left.right = Node(5)
    bt3.isequal(bt1)

test()