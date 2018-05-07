# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    #print('-',left,right);
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    #print('--',left,ave,right);
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)

    x = left;
    y = ave;
    #print('----',left,ave,right,a[left:right],number_of_inversions);
    for i in range(0,right-left):
        #print('-----',i,left,ave)
        if left < y and ( ave >= right or a[left]  <= a[ave] ):
            b[x+i] = a[left]
            left += 1;
        elif ave < right:
            b[x+i] = a[ave];
            #print('-->',a[ave],left,ave);
            if a[ave] < a[left]:
                number_of_inversions += (y-left)
                #print('---->noi:',number_of_inversions);
            ave += 1;

    a[x:right] = b[x:right];
    #print('---',a[x:right],number_of_inversions)
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
    #print(b);
