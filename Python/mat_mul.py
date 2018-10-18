# Uses python3
import sys
import math

# matrix chain multiplication, cost and order

# build dp matrix
def dp_mat(nom,d):
    mat = [ [0 for y in range(nom)] for x in range(nom)]
    pretty_print(mat,nom)

    for m in range(1,nom):
        for j in range(m,nom):
            i = j-m
            mat[i][j] = math.inf

            for k in range(i,j):
                mat[i][j] = min(mat[i][j], mat[i][k] + mat[k+1][j] + d[i]*d[k+1]*d[j+1])
                print(i,j," => ",k," ==> ",mat[i][j])
            else:
                print("------------")

    pretty_print(mat,nom)
    return mat;


def pretty_print(mat,w):
    print('============================\n')

    for w in range(w):
        print(w,end=' ')
    print()
    print('-' * 20)

    for x in mat:
        for y in x:
            print(y,end=' ')
        print()

def test():
    nom = 4
    dimensions = [5,4,6,2,7]
    print('Test set')
    print(nom,dimensions)
    mat = dp_mat(nom,dimensions)
    print('minimum cost',mat[0][nom-1])

def main():
    input = sys.stdin.read()
    nom, *dimensions = list(map(int, input.split()))
    mat = dp_mat(nom,dimensions)
    print(mat[0][nom-1])

if __name__ == '__main__':
    test()
    #main()
