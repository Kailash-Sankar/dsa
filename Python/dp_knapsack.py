# Uses python3
import sys

def greedy_knap(W, w):
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result

# build knapsack matrix, weights on y-axis, items on x-axis
def mat_knap(w,noi,weights,values):
    mat = [ [0 for y in range(w+1)] for x in range(noi)]
    pretty_print(mat)
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

    pretty_print(mat)
    return mat[noi-1][w]


def pretty_print(mat):
    print('============================\n')

    for w in range(10+1):
        print(w,end=' ')
    print()
    print('-' * 20)

    for x in mat:
        for y in x:
            print(y,end=' ')
        print()


def test():
    w = 10
    noi = 5
    weights = [3,5,3,3,5]
    values = [3,5,3,3,5]
    print("result - {}".format(mat_knap(w,noi,weights,values)))

def main():
    input = sys.stdin.read()
    w, noi, *weights = list(map(int, input.split()))
    print(mat_knap(w,noi,weights,weights))


if __name__ == '__main__':
    test()
    #main()
