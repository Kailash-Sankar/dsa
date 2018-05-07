# Uses python3
import sys
from collections import namedtuple
from operator import attrgetter

Segment = namedtuple('Segment', 'start end')

def create_set(segment):
    return set(range(segment.start,segment.end+1));

def optimal_points(n,segments):
    points = []

    # build sets for our segments
    sets = [];
    for seg in segments:
        sets.append(create_set(seg));

    i = 0;
    while i < n:
        if i+1 < n:
            int = sets[i] & sets[i+1];
            if int:
                sets[i+1] = int
                i+=1;
                continue;

        points.append(sets[i].pop())
        i+=1;

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n,*data = list(map(int, input.split()))

    segments = [];
    for i in range(0,n*2,2):
        segments.append(Segment(data[i],data[i+1]))

    segments.sort(key=attrgetter('start'))
    points = optimal_points(n,segments)
    print(len(points))
    for p in points:
        print(p, end=' ')


# 7
# 1 4 5 8 49 52 54
