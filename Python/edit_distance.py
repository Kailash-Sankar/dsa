# Uses python3
import time
import random
import string
import numpy as np

def edit_distance(s, t):
    sl = len(s)
    tl = len(t)
    
    # build matrix
    edMat = [ [0 for x in range(tl+1)] for y in range(sl+1) ]
    
    # first row
    for m in range(sl+1):        
        edMat[m][0] = m
    
    # first col
    for n in range(tl+1):
        edMat[0][n] = n;
    
    for i in range(1,sl+1):
        for j in range(1,tl+1):
            
            # previous values
            d = edMat[i-1][j-1]
            h = edMat[i-1][j]
            v = edMat[i][j-1] 
            
            # shortest move
            acts = (d,h,v)
            opt = min(acts)
            step = acts.index(min(acts))
            
            if step == 0 and s[i-1] == t[j-1]:
                edMat[i][j] = opt + 0;                
            else:
                edMat[i][j] = opt + 1; 
        
    # 2d array view
    #op = np.array(edMat)
    #print(op)        
    
    # build alignment
    optimal_alignment(edMat,s,t);
    
    return edMat[len(s)][len(t)];

def optimal_alignment(e,s,t):
    se = []
    te = []
    i = len(s)
    j = len(t)
    lcs = []

    while i+j > 0:
        pos = e[i][j]

        d = h = v = math.inf

        if i-1 >= 0 and j-1 >= 0:
            d = e[i-1][j-1]
        if i-1 >= 0:
            h = e[i-1][j]
        if j-1 >= 0:
            v = e[i][j-1]

        acts = (d,h,v)
        step = acts.index(min(acts))

        # diagonal, match or mismatch
        if step == 0:
            se.append(s[i-1])
            te.append(t[j-1])
            i=i-1
            j=j-1

            if s[i] == t[j]:
                lcs.append(s[i])

        # horizontal, deletion
        elif step == 1:
            se.append(s[i-1])
            te.append('-')
            i=i-1;
        # vertical, insertion
        else:
            se.append('-')
            te.append(t[j-1])
            j=j-1

    print(list(reversed(se)))
    print(list(reversed(te)))
    print('longest common subsequence',lcs)
    #return list(reversed(lcs));

def main():
    print(edit_distance(input(), input()))

def getString(l):
    return ''.join([random.choice(string.ascii_lowercase) for x in range(l)])

def test():
    s1 = 'ysebywznln' #getString(10);
    s2 = 'pvrizcwlzn' #getString(10);
    print('input:',s1,s2);
    start_time = time.time()
    ed = edit_distance(s1,s2)
    print('output:',ed,'time:',time.time()-start_time)

if __name__ == "__main__":
    test()
