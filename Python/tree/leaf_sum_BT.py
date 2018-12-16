# total tree sum
# max root to leaf sum with path
# max leaf to leaf sum with path
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
        
    # pretty print
    def pp(self):        
        self.levelBFT(self.root,0)
        nol = len(self._h)
        print('='*10)
        for i in sorted(self._h.keys()):
            print('-' * nol,self._h[i],'-' * nol)
            nol -= 1
            
    # find the max sum of the path to a leaf node    
    def maxLeafSum(self):
        if self.root is None:
            print('tree is empty')
            return
        self._maxSum = 0
        self._maxPath = []
        self._findSum(self.root,0)
        print('Path to max',self._maxPath)
        return self._maxSum

    # depth first traversal while maintaining sum
    # upong hitting leaf, returns while building path if sum is max
    def _findSum(self,node,sum):
        if node is not None:
            sum += node.val
            # left node
            if node.left is None and node.right is None:
                # new max sum    
                if sum > self._maxSum:
                    self._maxSum = sum;
                    self._maxPath = [node.val]                    
                    return 1
            else:                
                l = self._findSum(node.left,sum)
                r = self._findSum(node.right,sum)
                if l or r:
                    self._maxPath.append(node.val)
                    return 1                   
        return
    
    # leaf to leaf max sum and path taken
    def maxLeaftoLeafSum(self):
        self._maxLS = 0
        self._pathLS = []
        self._findLS(self.root)
        print('leaf to leaf path',self._pathLS)
        return self._maxLS;
    
    def _findLS(self,node):
        if node is not None:            
            # leaf node
            if node.left is None and node.right is None:
                return (node.val,[node.val])
            else:
                l,lpath = self._findLS(node.left)
                r,rpath = self._findLS(node.right)
                temp = node.val + l + r
                
                if temp > self._maxLS:
                   self._maxLS = temp
                   self._pathLS = [*lpath,node.val,*rpath]                   
                   
                if l > r:
                    return (node.val + l,[node.val,*lpath])
                else:
                    return (node.val + r,[node.val,*rpath])        
        return (0,[])
    
    # returns the sum of the whole tree
    def sum(self):
        if self.root is None:
            print('tree is empty')
            return
        return self._nodeSum(self.root)
    
    def _nodeSum(self,node):
        if node is not None:            
            # leaf node
            if node.left is None and node.right is None:
                return node.val
            else:
                l = self._nodeSum(node.left)
                r = self._nodeSum(node.right)
                return node.val + l + r
        return 0
        
def test():
    print('--- test case 1 ---')
    btree = BT();
    btree.root = Node(1);
    btree.root.left = Node(2)
    btree.root.right = Node(-3)
    btree.root.left.left = Node(4)
    btree.root.left.right = Node(5)
    btree.root.right.left = Node(6)
    btree.root.right.right = Node(7)
    btree.pp()
    print('max path to leaf sum',btree.maxLeafSum())
    print('max left to leaf sum', btree.maxLeaftoLeafSum())
    print('tree total sum', btree.sum())
    
    print('--- test case 2 ---')
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
    print('max path to leaf sum',bt1.maxLeafSum())
    print('max left to leaf sum', bt1.maxLeaftoLeafSum())
    print('tree total sum', bt1.sum())
    
test()