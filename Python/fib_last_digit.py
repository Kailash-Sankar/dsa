#Uses python3
def get_fibonacci_last_digit_naive(n):
    ar = [0, 1]
    if n <= 1:
        return ar[n];
    else :
        for i in range(2, n + 1):
            ar.append((ar[i - 1] + ar[i - 2]) % 10)
    return ar[n];

n = int(input())
print(get_fibonacci_last_digit_naive(n))
