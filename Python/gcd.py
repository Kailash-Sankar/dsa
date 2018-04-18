# Uses python3
'''
find the greatest common divisor of two numbers
'''
def gcd_opt(a, b):
    if b <= 1:
        return a if b == 0 else b;

    x  = a % b;
    return gcd_opt(b,x)

if __name__ == "__main__":
    input = input()
    a, b = map(int, input.split())    
    if b > a:
        a, b = b, a;
    print(gcd_opt(a, b))
