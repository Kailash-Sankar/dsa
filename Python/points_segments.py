# Uses python3
import sys

from collections import namedtuple
from operator import attrgetter

Segment = namedtuple('Segment', 'start end')

def fast_count_segments(segments, points):
    cnt = [0] * len(points)
    sec = segments[:];
    sec.sort(key=attrgetter('end'))

    for i in range(0,len(points)):
        m = binary_search(segments,points[i],'start')
        print('-',points[i],'spot',m);
        if m >= 0:
            exc = binary_search(sec,points[i],'end')
            print('-->',exc);
            cnt[i] = m - exc;
    return cnt

def binary_search(s,x,key):
    left,right = 0,len(s)-1;

    while left <= right:
        mid = left + ( right-left ) // 2
        if x == getattr(s[mid],key):
            # if lower bound, +1
            if key == 'start':
                mid+=1;
                print('bounds',left,right);
            return mid;
        elif x > getattr(s[mid],key):
            left=mid+1;
        else:
            right=mid-1;

    print(key,'::',left,right);
    return left;

def naive_count_segments(s, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(s)):
            if s[j].start <= points[i] <= s[j].end:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    segments = [];

    for i in range(2 ,n*2+2,2):
        segments.append(Segment(data[i],data[i+1]))
    segments.sort(key=attrgetter('start'))

    points = data[2 * n + 2:]
    if len(segments) <= 1:
        cnt = naive_count_segments(segments, points)
    else:
        cnt = fast_count_segments(segments, points)

    for x in cnt:
        print(x, end=' ')
