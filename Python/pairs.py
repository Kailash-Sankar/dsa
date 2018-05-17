#Uses python3
import sys
import math
import numpy as np
import time
import random

# another optimized solution
import ex_pairs

def minimum_distance(s):    
    # calculate euclidean distance
    if len(s) <= 3:
       return naive(s)
    
    # recursively find d
    mid = len(s)//2;   
    dl = minimum_distance(s[:mid])
    dr = minimum_distance(s[mid:])
    
    # minimum distance    
    d = min(dl,dr)
       
    # points along mid 
    c = [];    
    for i in range(0,len(s)):        
        if abs(s[mid,0] - s[i,0]) <= d:
            c.append(s[i]);
    
    # crossover distance
    if len(c) > 1:
        d = strip_distance(np.array(c),d);        
    
    return d;
   

def strip_distance(s,d):
    # sort along y-axis
    s = s[s[:,1].argsort()]    
    
    # find minimum distance
    for i in range(0,len(s)):
        lmt = min(i+7,len(s))
        for j in range(i+1,min(i+8,len(s))):
            if abs(s[i,1] - s[j,1]) <= d:
                dx = euclidean(s[i],s[j])
                d = min(d,dx);            
    return d;

def naive(s):
    d = [];
    for i in range(0,len(s)):
        for j in range(i+1,len(s)):
            d.append(euclidean(s[i],s[j]))            
    return min(d)

def euclidean(p,q):       
    pq  = np.sum(np.square(p-q))
    pqx = np.sqrt(pq)    
    return pqx;

def run_test():
    x_limit = 10**5
    y_limit = 10**5
    data = [random.randint(10,20)]
    
    print('==============================');
    print('Test size',data[0]);
    for i in range(0,data[0]):
        data.append(random.randint(-1*x_limit,x_limit))
        data.append(random.randint(-1*y_limit,y_limit))
    #print('Test data',data);
    
    #custom tests
    #data = [13, 9, -10, 2, 10, -8, 1, 8, 4, -10, 2, 2, 1, -4, 6, -4, -7, -1, -3, -6, 8, -9, 9, -4, -2, 5, -7]       
    s = extract_data(data);
    
    # naive
    start_time = time.time()
    md1 = naive(s)
    naive_time = time.time()
    
    # optimized
    s = s[s[:,0].argsort()]      
    md2 = minimum_distance(s)
    opt_time = time.time()
    
    #optimized2    
    x,y = s[:,0],s[:,1]    
    md3 = ex_pairs.solution(x,y)
    opt_time2 = time.time()
    
    # results
    print("Naive: {0:.9f}".format(md1),'time: ',naive_time - start_time)
    print("Optz1: {0:.9f}".format(md2),'time: ',opt_time - naive_time)
    print("Optz2: {0:.9f}".format(md3),'time: ',opt_time2 - opt_time)
    
    return md2-md3;

def extract_data(data):
    return np.array(list(zip(data[1::2],data[2::2])),dtype='int64')

def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    s = extract_data(data)
    print("{0:.9f}".format(minimum_distance(s)))    

if __name__ == '__main__':
    for i in range(0,10):
        if run_test() !=0 :
            break;
    print('Ran',i+1,'Tests');
    #data = main()

    


