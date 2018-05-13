#Uses python3
import sys
import math
import numpy as np

def minimum_distance(x, y):
    return 42;


def naive(x,y):
    d = [];
    for i in range(0,len(x)):
        for j in range(i,len(y)):
            d.append( euclidean((x[i],y[i]),(x[j],y[j])) );
    return min(d)

def euclidean(p,q):
    diff = np.square(p) - np.square(q)
    pq = np.absolute(np.sum(diff))
    pqx = np.sqrt(pq)
    return pqx

def run_test():
    data = [11,4,4,-2,-2,-3,-4,-1,3,2,3,-4,0,1,1,-1,-1,3,-1,-4,2,-2,4]
    return data;

def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    return data

if __name__ == '__main__':
    data = run_test()
    #data = main()
    n = data[0]
    x = np.array(data[1::2])
    y = np.array(data[2::2])

    #md = minimum_distance(x, y)
    md = naive(x,y)

    print("{0:.9f}".format(md))
