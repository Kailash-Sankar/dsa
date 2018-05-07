# Uses python3
import sys

from collections import namedtuple
from operator import attrgetter
import random


Segment = namedtuple('Segment', 'start end')

def fast_count_segments(segments, points):
    cnt = [0] * len(points)
    sec = segments[:];
    sec.sort(key=attrgetter('end'))

    for i in range(0,len(points)):
        m = binary_search(segments,points[i],'start')
        #print('-',points[i],'spot',m);
        if m >= 0:
            exc = binary_search(sec,points[i],'end')
            #print('-->',exc);
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
                #print('bounds',left,right);
            return mid;
        elif x > getattr(s[mid],key):
            left=mid+1;
        else:
            right=mid-1;

    #print(key,'::',left,right);
    return left;

def naive_count_segments(s, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(s)):
            if s[j].start <= points[i] <= s[j].end:
                cnt[i] += 1
    return cnt


def extract_data(data):
    n = data[0]
    m = data[1]
    segments = [];

    for i in range(2 ,n*2+2,2):
        segments.append(Segment(data[i],data[i+1]))
    segments.sort(key=attrgetter('start'))

    points = data[2 * n + 2:]

    return (segments,points)


def build_test_data(s,p):
    data = [s,p]
    for i in range(2,2*s+2,2):
        data.append(random.randrange(-100000000,100000000))
        data.append(random.randrange(data[i],100000000))

    for j in range(2*s+2,2*s+2+p):
        data.append(random.randrange(-100000000,100000000))

    return data;

def run_test():
    data = build_test_data(5000,1000);
    (segments,points) = extract_data(data);

    print('input',segments,points);
    cnt1 = naive_count_segments(segments, points)
    cnt2 = fast_count_segments(segments, points)

    f = 0;
    for i in range(0,len(points)):
        print(points[i],':',cnt1[i],cnt2[i])
        if cnt1[i] != cnt2[i]:
            f+=1;
    print("errors:",f);


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    (segments,points) = extract_data(data)

    if len(segments) <= 1:
        cnt = naive_count_segments(segments, points)
    else:
        cnt = fast_count_segments(segments, points)

    for x in cnt:
        print(x, end=' ')


if __name__ == '__main__':
    main();
    #run_test();
