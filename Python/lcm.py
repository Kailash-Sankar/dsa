# Uses python4
import sys

def gcd_opt(a, b):
    if b <= 1:
        return a if b == 0 else b;

    x  = a % b;
    return gcd_opt(b,x)

def lcm_opt(a,b):
    if b > a:
        a, b = b, a;
    gcd = gcd_opt(a,b)        
    lcm = int(a / gcd) * b
    return lcm;

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_opt(a, b))
