# Uses python2

'''
find the least common divisor of two numbers
'''
import sys

def gcd_opt(a, b):
    if b == 1:
        return b;
    x  = a % b;
    if x == 0:
        return b;
    else:
        return gcd_opt(b,x)

def lcm_opt(a,b):
    if b > a:
        a, b = b, a;
    gcd = gcd_opt(a,b)

    lcm = a / gcd * b
    return lcm;

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print lcm_opt(a, b)

