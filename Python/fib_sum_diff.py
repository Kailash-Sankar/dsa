#Uses python3
F = {0: 0, 1: 1, 2: 1}
def fib(n):
    if n in F:
        return F[n]
    f1 = fib(n // 2 + 1) % 10
    f2 = fib((n - 1) // 2) % 10
    F[n] = (f1 * f1 + f2 * f2 if n & 1 else f1 * f1 - f2 * f2) % 10
    return F[n]

[m,n] = map(int,input().split())
if n == m :
    diff = fib(n) % 10;
else:
    sum1 =  ( fib(n+2) - 1 )
    sum2 = ( fib(m+1) - 1 )
    print(n,sum1)
    print(m,sum2)
    print('diff',sum1-sum2)
    diff = ( sum1 - sum2 ) % 10

print(diff);
