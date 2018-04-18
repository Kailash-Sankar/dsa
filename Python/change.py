# Uses python2
import sys

def get_change(m):
    s = 0

    if m <= 0:
        return 0

    if m >= 10:
        s = m/10 + get_change(m%10)
    elif m >= 5:
        s = m/5 + get_change(m%5)
    else :
        s = m

    return s

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print get_change(m)
