class Node:
    def __init__(self,val):
        self.val = val
        self.left =  None
        self.right = None

class BT:
    def __init__(self):
        self.root = None
        
    # traverse bread first way while maintaining levels
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
        print('horizontal left-right slices',self._h)
        
    # find a node along with path
    def findNode(self,value):
        self.path = []
        if self.root is None:
            print('tree is empty')
        else:
            self._findNode(self.root,value)        
        print('->'.join(str(x) for x in self.path[::-1]))
        return self.path[::-1];
    
    def _findNode(self,node,value):
        if (node.val == value) \
            or (node.left and self._findNode(node.left,value)) \
            or (node.right and self._findNode(node.right,value)):
            self.path.append(node.val)
            return 1
        
        return None
    
    def findLCA(self,a,b):
        path_a = self.findNode(a);
        path_b = self.findNode(b);
        
        for i in range(0,len(path_a)):
            if path_a[i] == path_b[i]:
                continue
            else:
                break
        print('Lowest Common Ancestor of {} and {} is {}'.format(a,b,path_a[i-1]))
            
        
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
    btree.root.right.right.right = Node(67)
    btree.root.right.right.right.left = Node(22)
        
    btree.levelBFT(btree.root,0)
    btree.findNode(22)
    
    btree.findLCA(6,7)

test()