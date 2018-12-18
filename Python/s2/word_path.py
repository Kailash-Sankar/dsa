# Find the shortest path from one word to another word
# CAT -> CAP -> MAP -> MOP

# import list fo words from a file
def getWordList():
    words = []
    with open('words.txt') as f:
        line = f.readline().strip()
        while line:
            w = line.split()[0]
            words.append(w);
            line = f.readline()
    print('imported {} words'.format(len(words)))
    return words;

# node object with word and children who are 1 character away
class Node:
    def __init__(self,word):
        self.value = word
        self.children = []

    def __repr__(self):
        return 'Node: {} with {} children'.format(self.value,len(self.children))

# build relationship among nodes
# a graph with cycles
def buildGraph(words):
    nodes = {}
    # create nodes
    for word in words:
        nodes[word] = Node(word)

    # build realtionship among nodes with distance 1
    for node in nodes.values():
        for word in words:
            hd =  hammingDistance(node.value,word)
            if hd == 1:
                node.children.append(nodes[word])
    return nodes;

# distance between two strings of equal length
def hammingDistance(a,b):
    hd = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            hd += 1
    return hd

# find the shortest path between two nodes
def findMinPath(nodes,start,end):
    head = nodes[start]
    q = [head,'-']
    level = 0
    visited = {}
    found = 0

    # level order traversal
    while len(q) > 0:
        node = q.pop(0)
        # increment when the level marker is found
        if node == '-':
            if len(q) > 0:
                level += 1
                q.append('-')
            continue;

        # if the node was visited before, skip iteration (because we have cycles)
        if node.value in visited:
            continue;

        # break if destination word is found
        if node.value == end:
            found = 1
            break;
        else:
            visited[node.value] = len(node.children) or 1
            q.extend(node.children)

    if found:
        print('Path from {} to {} takes {} steps'.format(start,end,level))
        print(visited,len(visited))
    else:
        print('No path from {} to {}'.format(start,end))


def main(tests):
    words = getWordList();
    nodes = buildGraph(words)
    #print(nodes.values())

    for test in tests:
        findMinPath(nodes,*test)


def test():
    tests = [('CAT','BAT'),('CAT','MOP')]
    main(tests)

test()
