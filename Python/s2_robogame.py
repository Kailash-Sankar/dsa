# python3

# print matrix
def pretty_print(d,size):
    #return None
    for i in range(1,size+1):
        for j in range(2):
            print(d[i][j],end=' ')
        print()

# smoke
def test():
    test_case = [
        '4',
        '....',
        '.2.....',
        '.2...2..',
        '1.1.1.'
    ]
    execute(test_case)

def main():
    inp = sys.stdin.read().split('\n')
    execute(inp)


# parse input and execute the actions in order
def execute(inp):
    # iterate each test case
    for i in range(0,int(inp[0])):
        path = list(inp[1+i])
        arr = [0 for x in range(0,len(path))]
        safe = 1
        # iterate for each itemt
        for pos in range(0,len(path)):
            value = path[pos]
            if value == '.':
                continue
            else:
                m = int(value)
                if not marker(arr,pos,m):
                    safe = 0
                    break;
        if safe:
            print(inp[1+i]," => safe")
        else:
            print(inp[1+i]," => unsafe")


def marker(arr,pos,m):
    for i in range(1,m+1):
        if arr[pos-i] or arr[pos+i]:
            return 0
        else:
            arr[pos-i] = 1
            arr[pos+i] = 1
    return 1;


if __name__ == '__main__':
    test()
    #main()
