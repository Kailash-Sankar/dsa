# Uses python3
import sys
'''
find the mod of a huge fibonacci number
'''

#Optimized pisano logic from Marc Renault's blog
def opt_pisano(m):
    a=0
    b=p=1

    while b != 0:
        c= (a+b)%m
        a,b = b,c
        p = p + 1

    if p % 2 == 1:
        p = p*4;
    elif c != 1:
        p = p*2;

    return p;


#find smaller fib numbers
def alt(n,m):
    ar = [0,1]

    for i in range(2,n+1):
        ar.append( (ar[i-1] + ar[i-2]) % m )

    return ar[n];


#find pisano period of m
#find fib(n mod m) mod m
def find_fib_mod(n,m):
    if n <= 1:
        return n;
    p = opt_pisano(m)
    print('pisano',p)
    x = n % p;
    print('mod',x)
    y = alt(x,m)

    return y;

if __name__ == '__main__':
    input = sys.stdin.read();

    n, m = map(int, input.split())
    if n > m:
        print(find_fib_mod(n,m))
    else :
        print(alt(n,m))
