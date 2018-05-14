#Uses python3
import sys
import math
import numpy as np
import time
import random

def minimum_distance(s):
    #print('---')
    #print(s)
    
    # calculate euclidean distance
    if len(s) <= 3:
       return naive(s)
    
    # recursively find d
    mid = len(s)//2;   
    dl = minimum_distance(s[:mid])
    dr = minimum_distance(s[mid:])
    
    #print('-->',dl,dr);
    # minimum distance    
    d = min(dl,dr)
       
    # find crossover distances
    c = [];
    #print('mid x',s[mid,0]);
    for i in range(0,len(s)):
        #print('--diffs',s[mid,0],s[i,0]);
        if abs(s[mid,0] - s[i,0]) < d:
            c.append(s[i]);
    
    #print('==>',c,d);
    if len(c) > 0:
        d = strip_distance(np.array(c),d);        
    #print('==>dx:',d);
    
    return d;
   

def strip_distance(s,d):    
    s = s[s[:,1].argsort()]
    #print(" -- strip data --",s);
    
    for i in range(0,len(s)):
        j = i+1;
        while j < len(s) and abs(s[i,1] - s[j,1]) < d:
            dx = euclidean(s[i],s[j])
            d= min(d,dx);
            j+=1
    return d;

def naive(s):
    d = [];
    for i in range(0,len(s)):
        for j in range(i+1,len(s)):
            d.append(euclidean(s[i],s[j]))            
    return min(d)

def euclidean(p,q):    
    diff = p-q
    sqr = np.square(diff)    
    pq = np.absolute(np.sum(sqr))
    pqx = np.sqrt(pq)
    #print('<>',p,q,diff,sqr,pq,pqx);
    return pqx

def run_test():
    x_limit = 10**1
    y_limit = 10**9
    data = [random.randrange(2,10**3)]
    
    print('==============================');
    print('test size',data[0]);
    for i in range(0,data[0]):
        data.append(random.randrange(-1*x_limit,x_limit))
        data.append(random.randrange(-1*y_limit,y_limit))
    
    #custom tests
    #data = [3,5000,500,1,5000,-100,-100];
        
    s = extract_data(data);
    
    # naive
    start_time = time.time()
    md1 = naive(s)
    naive_time = time.time()
    
    # optimized
    s = s[s[:,0].argsort()]      
    md2 = minimum_distance(s)
    opt_time = time.time()   
    
    print("Naive: {0:.9f}".format(md1),'time: ',naive_time - start_time)
    print("Optimized: {0:.9f}".format(md2),'time: ',opt_time - naive_time)
    
    return md2-md1;

def extract_data(data):
    return np.array(list(zip(data[1::2],data[2::2])),dtype='int64')

def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    s = extract_data(data)
    print("{0:.9f}".format(minimum_distance(s)))    

if __name__ == '__main__':
    for i in range(0,101):
        if run_test() !=0 :
            break;
    print('Ran',i,'Tests');
    #data = main()

    


