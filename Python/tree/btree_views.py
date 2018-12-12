
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
    def verticalBFS(self,node,vline):
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

    def topView(self):
        t = []
        self.verticalBFS(self.root,0);
        for x in sorted(self._v.keys()):
            t.append(str(self._v[x][0]))
        print(' '.join(t))


def test():
    # test case 1
    # top view should be 4 2 1 3 7
    btree = BT();
    btree.root = Node(1);
    btree.root.left = Node(2)
    btree.root.right = Node(3)
    btree.root.left.left = Node(4)
    btree.root.left.right = Node(5)
    btree.root.right.left = Node(6)
    btree.root.right.right = Node(7)
    btree.topView();

    # test case 2
    # tpo view should be 2 1 3 6
    bt = BT()
    bt.root = Node(1)
    bt.root.left = Node(2)
    bt.root.right = Node(3)
    bt.root.left.right = Node(4)
    bt.root.left.right.right = Node(5)
    bt.root.left.right.right.right = Node(6)
    bt.topView();

test();
