# Uses python3
import sys
import math
import re

# matrix chain multiplication, cost and order

# build dp matrix
def dp_mat(nom,d,o):
    mat = [ [d[y] if y==x else 0 for y in range(nom)] for x in range(nom)]
    mit = [ [d[y] if y==x else 0 for y in range(nom)] for x in range(nom)]
    
    #pretty_print(mat,nom)

    for m in range(1,nom):
        for j in range(m,nom):
            i = j-m
            
            mat[i][j] = -1 * math.inf
            mit[i][j] = math.inf

            for k in range(i,j):
                temp1 = act(mat[i][k],o[k],mat[k+1][j])
                temp2 = act(mat[i][k],o[k],mit[k+1][j])
                temp3 = act(mit[i][k],o[k],mat[k+1][j])
                temp4 = act(mit[i][k],o[k],mit[k+1][j])
                
                mat[i][j] = max(mat[i][j],temp1,temp2,temp3,temp4)
                mit[i][j] = min(mit[i][j],temp1,temp2,temp3,temp4)
                
                #print(i,j," => ",k," ==> ",mat[i][j],mit[i][j])
            else:
                None
                #print("------------")

    #pretty_print(mat,nom)
    #pretty_print(mit,nom)
    return mat;

def act(a,op,b):
    result = {
      '+': lambda a,b: a + b,
      '*': lambda a,b: a * b,
      '-': lambda a,b: a - b
    }[op](a,b)
    return result

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

def eval_expr(e):
    inp = re.split(r"(\+|\-|\*)",e)
    numbers = []
    operators = []
    for n in range(0,len(inp)):
        if n%2==0:
            numbers.append(int(inp[n]))
        else:
            operators.append(inp[n])
    
    nom = len(numbers)
    
    #print(nom,numbers,operators)
    mat = dp_mat(nom,numbers,operators)
    return mat[0][nom-1]
   
def test():
    exp = '5-8+7*4-8+9'
    out = eval_expr(exp)
    print('Test set',exp)
    print('max value',out)
    
 
def main():
    input = sys.stdin.read()
    res = eval_expr(input)
    print(res)

if __name__ == '__main__':
    test()
    #main()
    


