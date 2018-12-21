import math

# use elements from a and b in given order to build the provided sum (x)
# the goal is to find the max number of elements that we can fit in before crossing sum

def execTests():
    results = (6,1,6,1,6,6,8,7,8,9,12,8,2,8,13,1,5,10,4,10,7,4,5,8,6,10,4,9,7,2,13,5,11,3,3,6,5,7,5,3,7,14,14,8,0,8,5,2,11,9);
    with open('tests.txt') as f:
        lines = f.readlines();
    nt = int(lines.pop(0))
    for i in range(nt):
        x = int(lines.pop(0).strip().split()[2])
        a = list(map(int,lines.pop(0).strip().split()))
        b = list(map(int,lines.pop(0).strip().split()))

        #op = twoStacksGreedy(x,list(reversed(a)),list(reversed(b)))
        op = twoStacks(x,list(a),list(b))

        print('Test case {}'.format(i),end='')
        if op == results[i]:
            print('--> PASS')
        else:
            print('--> FAIL')
            print('=>',a,b,x)
            print(op,'-<>-',results[i])
            break;

# greedy approach fails
def twoStacksGreedy(x, a, b):
    sum = 0
    count = 0
    temp = []

    while sum <= x:
        # a and b should be non empty
        if  len(a) <=0 and len(b) <= 0:
            break;

        # pick smaller among a and b
        s1 = a[-1] if len(a) > 0 else math.inf
        s2 = b[-1] if len(b) > 0 else math.inf
        t = 0
        if s1 < s2:
            t = s1
            a.pop()
        else:
            t = s2
            b.pop()

        sum += t
        count += 1
        temp.append(t)

    print('tt-',temp)
    return count-1

# built the list only with elements from a first
# then iterate on elements from b and add to sum
# if sum is greater remove the last added element from b and so on
# [ a1 a2 a3 a4 a5 ] => [a1 a2 a3 b1 b2]
def twoStacks(x,a,b):
    sum = 0
    count = 0
    temp = []

    # sum from a
    for i in a:
        if sum + i > x:
            break
        sum += i
        temp.append(i)

    count = len(temp)
    _count = count

    # adding b while keeping or removing a
    for j in b:
        sum += j
        if sum <= x:
            count += 1
            continue
        else:
            if len(temp):
                sum -= temp.pop()
            else:
                break

    return count if count > _count else _count


execTests();
