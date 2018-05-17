# Uses python3
import sys
import random
import time

# change count stack
st = [0];

def get_change(m,d):   
    for money in range(1,m+1):
        count = money+1;
        for deno in d:
            if deno <= money:
                count = min(count,1 + get_count(money-deno))
        st.append(count)
    
    return st[m];

# lookup and return previous count
def get_count(money):   
    return st[money];    

def main():
    m = int(sys.stdin.read())
    d= [1,3,4];
    print(get_change(m,d))

def test():
    start_time = time.time()
    m = random.randint(1,100);
    d =[1,3,4];
    print('Input:: money:',m,'denomination:',d);
    c =get_change(m,d)    
    print('result:',c,'time:',time.time()-start_time);
     
if __name__ == '__main__':
    #main()
    test()
