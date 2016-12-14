# Uses python2
'''
find the greatest common divisor of two numbers
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

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    if b > a:
        a, b = b, a;
    print gcd_opt(a, b)