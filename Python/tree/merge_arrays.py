import math
from random import randint

def merge_arrays(al):
    noa = len(al)
    m = 0
    for x in range(0,noa):
        m += len(al[x])

    farr = [];
    indexes = [0] * noa;
    for i in range(0,m):
        min = math.inf
        pos = None
        for j in range(0,noa):
            indx = indexes[j]
            if indx < len(al[j]) and al[j][indx] < min:
                min = al[j][indx];
                pos = j;

        indexes[pos] += 1;
        farr.append(min)
    return farr;


def main():
    al = []
    for i in range (5):
        limit = randint(5,10);
        al.append( sorted([ randint(1,100) for x in range(limit) ]) )
        print('input array - {}'.format(i),al[i])
    farr = merge_arrays(al)
    print("output",farr);

if __name__ == '__main__':
    main()
