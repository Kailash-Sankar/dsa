# Uses python3
import sys
import operator

cr = []

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    #print capacity
    #print weights
    #print values

    #unit value per weight
    for i in range(0,len(weights)):
        #cr.append(float(values[i])/float(weights[i]))
        cr.append({ 'v' : values[i], 'w' : weights[i], 'vw' : float(values[i])/float(weights[i]) })

    #sort input
    cr.sort(key=operator.itemgetter('vw'), reverse=True)
    #print "Sorted Output: {0}". format(cr)

    #real steel
    for x in cr:
        if capacity <= x['w'] :
            value =  value + capacity * x['vw']
            break
        else :
            value = value + x['w'] * x['vw']
            capacity = capacity - x['w']

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print "{:.10f}".format(opt_value)
