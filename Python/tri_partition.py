# Uses python3
import sys
import math

# 2-partition and 3-partition problem

# build dp matrix, weights on y-axis, items on x-axis
def mat_knap(w,noi,weights,values):
    mat = [ [0 for y in range(w+1)] for x in range(noi)]
    pretty_print(mat,w)
    for i in range(noi):
        for j in range(w+1):
            opt1 = opt2 = 0;
            p = j

            # current item
            if weights[i] <= j:
                opt1 = values[i]
                p = j-weights[i] # remaining weight

            # current + value for remaining item from previous row
            if i-1 >= 0:
                opt1 = opt1 + mat[i-1][p] # row above or remaining weight
                opt2 = mat[i-1][j]

            mat[i][j] = opt1 if opt1 > opt2 else opt2;

    pretty_print(mat,w)
    return mat;


def pretty_print(mat,w):
    print('============================\n')

    for w in range(w+1):
        print(w,end=' ')
    print()
    print('-' * 20)

    for x in mat:
        for y in x:
            print(y,end=' ')
        print()

def test():
    weights = values = [1,2,3,4,5,5,7,7,8,10,12,19,25]
    noi = len(weights)
    w = sum(weights)
    print('Test set')
    print(w,weights)
    mat = mat_knap(w,noi,weights,values)
    # two partition
    di_part(mat,w,noi)
    # three partition
    tri_part(mat,w,noi)



def di_part(mat,w,noi):
    wh = int(math.ceil(w/2))
    print("result - {} : {}".format(mat[noi-1][w],mat[noi-1][w//2]))
    if mat[noi-1][w//2] == wh:
        print("data set can be 2-partitioned")
        return 1;
    else:
        print("data set cannot be 2-partitioned")
    return 0;


def tri_part(mat,w,noi):
    wh = int(math.ceil(w/3))
    p1 = w//3
    p2 = p1 * 2
    p3 = p2 + p1

    if p3 == w and mat[noi-1][p1] == p1 and mat[noi-1][p2] == p2 and mat[noi-1][p3] == p3 :
        print("data set can be 3-partitioned")
        return 1;
    else:
        print("data set cannot be 3-partitioned")
    return 0;

def main():
    input = sys.stdin.read()
    noi, *weights = list(map(int, input.split()))
    w = sum(weights)
    mat = mat_knap(w,noi,weights,weights)
    print(tri_part(mat,w,noi))


if __name__ == '__main__':
    #test()
    main()
