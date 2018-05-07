# Uses python3
import sys
import random

def partition2(a, l, r):
    x = a[l]
    j = l;
    e = 0;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]

            if a[i] == x:
                e += 1;
            else:
                a[j-e-1],a[j] = a[j],a[j-e-1]

    return (j,e)


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #print('pivot',a[l]);
    (m,n) = partition2(a, l, r)
    #print(a,m,n);
    #print('---');
    randomized_quick_sort(a, l, m - n - 1);
    randomized_quick_sort(a, m + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
