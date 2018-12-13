
class Node:
    def __init__(self,val):
        self.val = val
        self.left =  None
        self.right = None

class BT:
    def __init__(self):
        self.root = None

    # vertical slicing through DFS
    def vro(self):
        if self.root is None:
            print('empty')
        else:
            self._v = {}
            self._vertical(self.root,0)
        print('vertical slices',self._v)

    def _vertical(self,node,vline):
        if vline in self._v:
            self._v[vline].append(node.val)
        else:
            self._v[vline] = [node.val];

        if node.left is not None:
            self._vertical(node.left,vline-1)

        if node.right is not None:
            self._vertical(node.right,vline+1)

    # vertical slicing throgh BFS
    # traverse in a bread first way while maintaining horizontal distance
    # -1 to the left, +1 to the right
    def verticalBFT(self,node,vline):
        self._v = {}
        q = [(node,0)]
        while len(q) > 0:
            node,vline = q.pop(0)
            if vline in self._v:
                self._v[vline].append(node.val)
            else:
                self._v[vline] = [node.val];

            if node.left is not None:
                q.append((node.left,vline-1))

            if node.right is not None:
                q.append((node.right,vline+1))
        print('vertical top-down slices',self._v)

    # first element of vertical sliced list
    def topView(self):
        t = []
        self.verticalBFT(self.root,0);
        for x in sorted(self._v.keys()):
            t.append(str(self._v[x][0]))
        print('Top view:',' '.join(t))

    # last element of vertical sliced list
    def bottomView(self):
        t = []
        self.verticalBFT(self.root,0);
        for x in sorted(self._v.keys()):
            t.append(str(self._v[x][-1]))
        print('Bottom view:',' '.join(t))
           
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
        
    # first element of the level ordered list
    def leftView(self):
        t = []
        self.levelBFT(self.root,0);
        for x in sorted(self._h.keys()):
            t.append(str(self._h[x][0]))
        print('Left view:',' '.join(t))

    # last element of the level ordered list
    def rightView(self):
        t = []
        self.levelBFT(self.root,0);
        for x in sorted(self._h.keys()):
            t.append(str(self._h[x][-1]))
        print('right view:',' '.join(t))
    

def test():
    print('--- test case 1 ---')
    # top view should be 4 2 1 3 7
    # bottom view should be 4 2 6 3 7
    # left view should be 1 2 4
    # right view should be 1 3 7
    btree = BT();
    btree.root = Node(1);
    btree.root.left = Node(2)
    btree.root.right = Node(3)
    btree.root.left.left = Node(4)
    btree.root.left.right = Node(5)
    btree.root.right.left = Node(6)
    btree.root.right.right = Node(7)
    btree.topView();
    btree.bottomView();
    btree.leftView();
    btree.rightView();

    print('--- test case 2 ---')
    # top view should be 2 1 3 6
    # bottom view should be 2 4 5 6
    # left view should be 1 2 4 5 6
    # right view should be 1 3 4 5 6
    bt1 = BT()
    bt1.root = Node(1)
    bt1.root.left = Node(2)
    bt1.root.right = Node(3)
    bt1.root.left.right = Node(4)
    bt1.root.left.right.right = Node(5)
    bt1.root.left.right.right.right = Node(6)
    bt1.topView();
    bt1.bottomView();
    bt1.leftView();
    bt1.rightView();
                    
    
    print('--- test case 3 ---')
    # bottom view should be 5 10 3 14 25
    # left view should be 20 8 5 10
    bt2 = BT()
    bt2.root = Node(20)
    bt2.root.left = Node(8)
    bt2.root.right = Node(22)
    bt2.root.left.left = Node(5)
    bt2.root.left.right = Node(3)
    bt2.root.right.right = Node(25)
    bt2.root.left.right.left = Node(10)
    bt2.root.left.right.right = Node(14)
    bt2.bottomView();
    bt2.leftView();
    
    print('--- test case 4 ---')
    # bottom view should be 5 10 4 14 25
    # left view should be 20 8 5 10
    # right view should be 20 22 25 14
    bt3 = BT()
    bt3.root = Node(20)
    bt3.root.left = Node(8)
    bt3.root.right = Node(22)
    bt3.root.left.left = Node(5)
    bt3.root.left.right = Node(3)
    bt3.root.right.left = Node(4)
    bt3.root.right.right = Node(25)
    bt3.root.left.right.left = Node(10)
    bt3.root.left.right.right = Node(14)
    bt3.bottomView();
    bt3.leftView();
    bt3.rightView();

    
    

test();
