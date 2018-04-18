#Uses python3
def get_fibonacci_last_digit_naive(n):
    ar = [0, 1]
    if n <= 1:
        return ar[n];
    else :
        for i in range(2, n + 1):
            ar.append((ar[i - 1] + ar[i - 2]) % 10)
    return ar[n];

F = {0: 0, 1: 1, 2: 1}
def fib(n):
    if n in F:
        return F[n]
    f1 = fib(n // 2 + 1) % 10
    f2 = fib((n - 1) // 2) % 10
    F[n] = (f1 * f1 + f2 * f2 if n & 1 else f1 * f1 - f2 * f2)
    return F[n]

n = int(input())
sum2 =  ( fib(n+2) - 1 ) % 10;
print(sum2)
