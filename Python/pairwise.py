# uses python2
n = int( raw_input() );
assert( n >= 2 and n <= 2*10**5 )

num = [ int(x) for x in raw_input().split() ]
assert( len(num) == n )

m1 = m2 = 0

for x in num:
    if x >= m1:
        m2 = m1 #second largest
        m1 = x  #largest
    #in case the largest gets picked first and we never enter the above block
    elif x >= m2:
        m2 = x;

print m1 * m2


