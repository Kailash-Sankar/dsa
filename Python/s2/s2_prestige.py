# python3

# ignore zero of decks for ease
def build_decks(size,uf,lf):
    d1 = [ [ 1 if y == 0 else -1 for y in range(0,2)] for x in range(0,size+1)]
    uf.insert(0,'-')
    lf.insert(0,'-')
    d2 = [ [ uf[x] if y == 0 else lf[x] for y in range(0,2)] for x in range(0,size+1)]

    print('decks')
    pretty_print(d1,size)
    pretty_print(d2,size)

    return d1,d2

# flips and swaps between l and r postitions in reverse
def flip_deck(d2,l,r):
    temp = d2[l:r+1]
    temp.reverse();
    for i in range(0,r-l+1):
        d2[l+i] =[temp[i][1], temp[i][0]]

# perform magic calculation
def magic(d1,d2,act):
    z,a,b,c,d = act
    m = 0
    for x in range(0,b-a+1):
        m += d1[c+x][0] * d2[a+x][0]
    return m;

# print matrix
def pretty_print(d,size):
    #return None
    for i in range(1,size+1):
        for j in range(2):
            print(d[i][j],end=' ')
        print()

# smoke
def test():
    inp = [
        '7 9',
        '3 5 0 2 5 7 4',
        '2 8 4 4 0 1 6',
        '3 1 3 3 5',
        '2 1',
        '1 2 6',
        '1 2 7',
        '2 3',
        '3 1 5 3 7',
        '3 1 7 1 7',
        '1 1 6',
        '3 1 7 1 7'
    ];
    execute(inp);

def main():
    inp = sys.stdin.read().split('\n')
    execute(inp)

# parse input and execute the actions in order
def execute(inp):
    size,noa = list(map(int,inp[0].split(' ')))
    uf = list(map(int,inp[1].split(' ')))
    lf = list(map(int,inp[2].split(' ')))

    # build decks
    d1,d2 = build_decks(size,uf,lf)

    # actions
    for i in range(0,noa):
        act = list(map(int,inp[3+i].split(' ')))
        print('Performing action ',act)
        if act[0] == 1:
            flip_deck(d2,act[1],act[2])
            pretty_print(d2,size)
        elif act[0] == 2:
            flip_deck(d1,1,act[1])
            pretty_print(d1,size)
        elif act[0] == 3:
            print('magic ',magic(d1,d2,act))
        else:
            None
        print('-' * size)


if __name__ == '__main__':
    test()
    #main()
