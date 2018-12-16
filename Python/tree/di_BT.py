# find the diameter of a binary tree
class Node:
    def __init__(self,val):
        self.val = val
        self.left =  None
        self.right = None
# print diameter of a binary tree
class BT:
    def __init__(self):
        self.root = None
    
    def levelBFT(self,node,vline):
        self._h = {}
        q = [(node,0)]
        while len(q) > 0:
            node,vline = q.pop(0)
            if vline in self._h:
                self._h[vline].append(node.val)
            else:
                self._h[vline] = [node.val];

            if node.left is not None:
                q.append((node.left,vline+1))

            if node.right is not None:
                q.append((node.right,vline+1))
        
    # pretty print
    def pp(self):        
        self.levelBFT(self.root,0)
        nol = len(self._h)
        print('='*10)
        for i in sorted(self._h.keys()):
            print('-' * nol,self._h[i],'-' * nol)
            nol -= 1
            
    def diameter(self):
        if self.root is None:
            print('tree is empty')
            return
        self._diameter = 0
        self._di(self.root)
        return self._diameter;
    
    def _di(self,node):
        if node is not None:
            # leaf node
            if node.left is None and node.right is None:
                return 1;
            else:
                l = self._di(node.left)
                r = self._di(node.right)
                temp = l + r + 1
                if temp > self._diameter:
                    self._diameter = temp
                
                d = l if l > r else r
                return d+1
        return 0
            
            
def test():
    print('--- test case 1 ---')
    bt1 = BT()
    bt1.root = Node(-15)
    bt1.root.left = Node(5)
    bt1.root.right = Node(6)
    bt1.root.left.left = Node(-8)
    bt1.root.left.right = Node(1)
    bt1.root.left.left.left = Node(2)
    bt1.root.left.left.right = Node(6)    
    bt1.root.right.left = Node(3)
    bt1.root.right.right = Node(9)
    bt1.root.right.right.right = Node(0)
    bt1.root.right.right.right.left = Node(4)
    bt1.root.right.right.right.right = Node(-1)
    bt1.root.right.right.right.right.left = Node(10)
    bt1.pp();
    print('diameter of the tree',bt1.diameter())
    
    print('--- test case 2 ---')
    bt2 = BT()
    bt2.root = Node(1)
    bt2.root.left = Node(2)
    bt2.root.right = Node(3)
    bt2.root.left.left = Node(4)
    bt2.root.left.right = Node(5)
    bt2.pp()
    print('diameter of the tree',bt2.diameter())
    
    

test()