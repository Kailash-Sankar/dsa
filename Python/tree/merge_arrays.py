import math
from random import randint

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
    m = 0
    for x in range(0,noa):
        m += len(al[x])


    return farr;


def main():
    al = []
    for i in range (5):
        limit = randint(5,10);
        al.append( sorted([ randint(1,100) for x in range(limit) ]) )
        print('input array - {}'.format(i),al[i])
    
    farr = merge_arrays_naive(al)
    print("output",farr);
    
 
def heap():
    arr = [(5,0),(76,1),(88,2),(2,3),(9,4),(1,5)]
    n = len(arr)
   
    for i in range(n-1,-1,-1):
        heapify(arr,n,i)
        
    print('min heap',arr);
    
    return arr

# heapify for min heap
def heapify(arr,n,index):
    print('-',index,arr);
    l = 2*index + 1
    r = 2*index + 2
    
    min = index;
    if l < n and arr[index][0] > arr[l][0]:
        min = l;
    
    if r < n and arr[min][0] > arr[r][0]:
        min = r;
    
    
    if min != index:
        arr[index],arr[min] = arr[min],arr[index]
        
        # bubble down
        heapify(arr,n,min)


if __name__ == '__main__':
    heap()
