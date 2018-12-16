class Node:
    def __init__(self,val):
        self.val = val
        self.left =  None
        self.right = None

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
        #print('horizontal left-right slices',self._h)

    # mirrors the tree in place
    def mirrorMe(self):
        if self.root is None:
            print('tree is empty')
            return        
        self._mirrorTree(self.root)
        
    def _mirrorTree(self,node):
        if node is not None:
            self._mirrorTree(node.left)
            self._mirrorTree(node.right)
            
            temp = node.left
            node.left = node.right
            node.right = temp        
        return
    
    # returns a mirrored copy
    def mirror(self):
        if self.root is None:
            print('tree is empty')
            return        
        btm = BT()
        btm.root = self._mirrorCopy(self.root)
        return btm
    
    def _mirrorCopy(self,node):
        if node is not None:
            nn = Node(node.val)
            nn.right = self._mirrorCopy(node.left)
            nn.left =  self._mirrorCopy(node.right)                       
            return nn
        return None
    
    # checks if input tree is it's mirror
    def isMirror(self,node):
        t = self._ismirror(self.root,node.root)
        if t:
            print('Trees are mirrors');
        else:
            print('Trees are not mirrors');
        
    def _ismirror(self,a,b):
        if a is None and b is None:
              return 1;
        
        if a.val is not None and b is not None:                 
            if a.val == b.val:
                return self._ismirror(a.left,b.right) and self._ismirror(a.right,b.left)
        
        return 0             
               
    # pretty print
    def pp(self):        
        self.levelBFT(self.root,0)
        nol = len(self._h)
        print('='*10)
        for i in sorted(self._h.keys()):
            print('-' * nol,self._h[i],'-' * nol)
            nol -= 1
            
def test():
    print('--- test case 1 ---')
    btree = BT();
    btree.root = Node(1);
    btree.root.left = Node(2)
    btree.root.right = Node(3)
    btree.root.left.left = Node(4)
    btree.root.left.right = Node(5)
    btree.root.right.left = Node(6)
    btree.root.right.right = Node(7)
    btree.pp()
    btree.mirrorMe()    
    btree.pp()
    
    print('--- test case 2 ---')
    bt1 = BT()
    bt1.root = Node(1)
    bt1.root.left = Node(2)
    bt1.root.right = Node(3)
    bt1.root.left.right = Node(4)
    bt1.root.left.right.left = Node(5)
    bt1.root.left.right.right = Node(6)
    bt1.pp()
    bt2 = bt1.mirror();
    bt1.pp()
    bt2.pp()
    
    print('--- test case 2 ---')
    btree.isMirror(bt1);
    bt1.isMirror(bt2);
    
    print('--- test case 4 ---')
    bt3 = BT()
    bt3.root = Node(1)
    bt3.root.left = Node(2)
    bt3.root.right = Node(2)
    bt3.root.left.left = Node(3)
    bt3.root.left.right = Node(4)
    bt3.root.right.left = Node(4)
    bt3.root.right.right = Node(3)
    bt3.pp()
    # check if the tree is a mirror of itself
    bt3.isMirror(bt3);
    bt4 = bt3.mirror();
    bt4.pp()
    
test();