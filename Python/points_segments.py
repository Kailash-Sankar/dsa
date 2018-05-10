# Uses python3
import sys

import random
import numpy as np
import time

def fast_count_segments(nps, npe, points):
    cnt = [0] * len(points)
    nps.sort();
    npe.sort();

    for i in range(0,len(points)):
        m = binary_search(nps,points[i],'start')
        if m >= 0:
            exc = binary_search(npe,points[i],'end')
            cnt[i] = m - exc;
    return cnt

def binary_search(s,x,key):
    left,right = 0,len(s)-1;

    while left <= right:
        mid = left + ( right-left ) // 2
        if x == s[mid]:
            # for matches in start, get max index
            if key == 'start':
                left = mid+1;
            # for matches in end, get min index
            else:
                right = mid-1;

        elif x > s[mid]:
            left=mid+1;
        else:
            right=mid-1;

    return left;

def naive_count_segments(nps, npe, points):
    cnt = [0] * len(points)
    #return cnt;
    for i in range(len(points)):
        for j in range(len(nps)):
            if nps[j] <= points[i] <= npe[j]:
                cnt[i] += 1
    return cnt


def extract_data(data):
    n = data[0]
    nps = np.array(data[2:n*2+2:2]);
    npe = np.array(data[3:n*2+2:2]);
    points = data[2 * n + 2:]
    return (nps,npe,points)


def build_test_data():

    s = random.randrange(1,50000)
    p = random.randrange(1,50000)
    limit = 10**8 # set small range like 10, for equal values

    print('Test:',s,p);
    data = [s,p]
    for i in range(2,2*s+2,2):
        data.append(random.randrange(-1*limit,limit+1))
        data.append(random.randrange(data[i],limit+1))

    for j in range(2*s+2,2*s+2+p):
        data.append(random.randrange(-1*limit,limit))

    return data;

def run_test():
    data = build_test_data();
    (nps,npe,points) = extract_data(data);
    #print('inputs',nps,npe,points);

    cnt1 = naive_count_segments(nps,npe,points)
    naive_time = time.time()
    print("--- naive done: %s seconds ---" % (naive_time - start_time))

    cnt2 = fast_count_segments(nps,npe,points)
    print("--- fast done: %s seconds ---" % (time.time() - naive_time))

    f = 0;
    for i in range(0,len(points)):
        #print(points[i],':',cnt1[i],cnt2[i])
        if cnt1[i] != cnt2[i]:
            f+=1;
    print("errors:",f);


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    (nps,npe,points) = extract_data(data)

    if len(nps) <= 1:
        cnt = naive_count_segments(nps, npe, points)
    else:
        cnt = fast_count_segments(nps, npe, points)

    for x in cnt:
        print(x, end=' ')


if __name__ == '__main__':
    start_time = time.time()
    #main();
    run_test();
