# longest common subsequence

def findLCS(a,b):
    return _naiveLCS(a,b,len(a),len(b))

def _naiveLCS(a,b,i,j):
    if i == 0 or j == 0:
        return 0

    if a[i-1] == b [j-1]:
        return 1 + _naiveLCS(a,b,i-1,j-1)
    else:
        return max( _naiveLCS(a,b,i-1,j) , _naiveLCS(a,b,i,j-1) )

def matchLCS(a,b):
    m = len(b)
    n = len(a)
    mat = [ [ 0 for i in range(m+1)] for j in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i-1] == b[j-1]:
                mat[i][j] = 1 + mat[i-1][j-1]
            else:
                mat[i][j] = max(mat[i-1][j],mat[i][j-1])
    print('LCS Matrix')
    pretty_print(mat)
    le = mat[n][m]

    # print the match
    lcs = []
    x = n
    y = m
    while x > 0 and y > 0:
        if a[x-1] == b[y-1]:
            lcs.append(a[x-1])
            x -= 1;
            y -= 1;
        elif mat[x-1][y] > mat[x][y-1]:
            x -= 1;
        else:
            y -= 1;
    print('Match',''.join(lcs[::-1]))

def pretty_print(mat):
    for row in mat:
        print(row)


# lcs is GTAB
x = findLCS('AGGTAB','GXTXAYB');
print('Length of LCS',x)

matchLCS('AGGTAB','GXTXAYB')

matchLCS('ABCDGH','AEDFHR')
