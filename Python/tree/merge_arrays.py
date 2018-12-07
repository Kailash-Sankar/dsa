import math
from random import randint
import time

# merge n sorted arrays, navie and heap approach

def merge_arrays_naive(al):
    noa = len(al)
    m = 0
    for x in range(0,noa):
        m += len(al[x])

    farr = [];
    indexes = [0] * noa;
    for i in range(0,m):
        min = math.inf
        pos = None
        for j in range(0,noa):
            indx = indexes[j]
            if indx < len(al[j]) and al[j][indx] < min:
                min = al[j][indx];
                pos = j;

        indexes[pos] += 1;
        farr.append(min)
    return farr;

  
def merge_arrays_heap(al):
    noa = len(al)
    
    # size of final array
    m = 0
    for x in range(0,noa):
        m += len(al[x])
        
    # create a heap
    # and array position markers
    arr = []
    pos = []
    for i in range(noa):
        arr.append((al[i][0],i))
        pos.append(1);        
    heap(arr);   
    
    farr= []
    for j in range(m):
        # pop min value from heap
        farr.append(arr[0][0])
        
        # update marker and push in next
        arr_mark = arr[0][1]
        index_mark = pos[arr_mark]        
        if index_mark < len(al[arr_mark]):
            arr[0] = (al[arr_mark][pos[arr_mark]], arr_mark)
            pos[arr_mark] += 1
        else:
            arr[0] = (math.inf,arr_mark)
        heapify(arr,noa,0)           
           
    #print('op',arr);     

    return farr;
    
# convert array to heap
def heap(arr):    
    n = len(arr)
   
    #print('input array',arr);
    for i in range(n-1,-1,-1):
        heapify(arr,n,i)
        
    #print('min heap',arr);
    
    return arr

# heapify for min heap
def heapify(arr,n,index):
    #print('-',index,arr);
    l = 2*index + 1
    r = 2*index + 2
    
    #print('heapify-',index,l,r);
    
    min = index;
    if l < n and arr[index][0] > arr[l][0]:
        min = l;
    
    if r < n and arr[min][0] > arr[r][0]:
        min = r;
    
    
    if min != index:
        arr[index],arr[min] = arr[min],arr[index]
        
        # bubble down
        #print('bubble down',index,min)
        heapify(arr,n,min)


def main():
    al = []
    for i in range (100):
        limit = randint(250,500);
        al.append( sorted([ randint(1,100) for x in range(limit) ]) )
        #print('input array - {}'.format(i),al[i])
        print('input array - {}:'.format(i),len(al[i]))
    
    # nave approach
    start_nv = time.time()
    farr1 = merge_arrays_naive(al)
    end_nv = time.time()
    #print("naive_output",farr1);
    print("navie time",end_nv - start_nv);
    
    # optimized approach
    start_op = time.time()
    farr2 = merge_arrays_heap(al)
    end_op = time.time()
    #print("optimzed_output",farr2);
    print("optimized time",end_op - start_op)
    
    #verify outputs
    try:
        if len(farr1) == len(farr2):
            for i in range(len(farr1)):
                if farr1[i] != farr2[2]:
                    Exception('Value mismatch on index {}'.format(i));
        else:
            raise Exception('Length mismatch');
    except Exception as error:
        print('Verification failed',error);
        

def test():
    arr = [(5,0),(76,1),(88,2),(2,3),(9,4),(1,5)]
    heap(arr)
    
if __name__ == '__main__':   
    main()
