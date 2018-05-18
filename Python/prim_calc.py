# Uses python3
import sys
import time
import random

def greedy_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def dynamic_sequence(n):
    seq = [0,0];
    indices =[0,1];
    
    # build up array of operation counts
    for i in range(2,n+1):     
        s1 = 1 + seq[i-1];        
        s2 = 1 + i%2 + seq[i//2];        
        s3 = 1 + i%3 + seq[i//3];
        
        # min operation
        s = min(s1,s2,s3);
        x = (s1,s2,s3).index(s) + 1;
        
        # store the index that led here
        seq.append(min(s1,s2,s3));
        indices.append(i -1 if x == 1 else i//x); 
    
    # trace the way back
    way = [];
    j = len(indices)-1;
    while j > 1:
        way.append(j);
        j = indices[j];    
    way.append(j);
    
    return reversed(way);
    
def main():
    input = sys.stdin.read()
    n = int(input)
    return list(dynamic_sequence(n))    
        
def test():
    start_time = time.time();
    n = random.randint(1,10**6);
    print('Input:',n);
    sequence = list(dynamic_sequence(n));
    print('Time:',time.time() - start_time);
    return sequence;

if __name__ == '__main__':
    sequence = test()
    #sequence = main()
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')