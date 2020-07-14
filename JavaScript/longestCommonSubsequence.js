
// write a program to find the longest common subsequence
// ABAZDC, BACBAD => ABAD
// AGGTAB, GXTXAYB => GTAB
// aaaa, aa => aa

/*
recursive solution will have exponential complexity O(2 ** max(m,n))
dynamic programming solution can be solved in O(mn)

build a matrix of size m+1, n+1, start with 0 in 0th row and column
- in case of a match, the value is previous diagonal  + 1
- if there's no match, the value is max(previous row, previous column)

Using the previous values is equivalent to memoization

  - B A C B A D
- 0 0 0 0 0 0 0
A 0 0 1 1 1 1 1
B 0 1 1 1 2 2 2
A 0 1 2 2 2 3 3  
Z 0 1 2 2 2 3 3
D 0 1 2 2 2 3 4
C 0 1 2 3 3 3 4

The last value is the size of LCS
Backtrack the matrix and find elements where the value shifts diagonally to a lower value
=> A B A D
*/


function lcs(strA, strB) {
    const m = strA.length;
    const n = strB.length;

    // build the matrx
    const mat = [];
    for(let i=0; i<= m; i++) {
        mat.push(Array(n+1).fill(0));
    }

    // populate based on the logic above
    for(let x=1; x<=m; x++) {
        for(let y=1; y<=n; y++) {
            if( strA[x-1] === strB[y-1] ) {
                mat[x][y] = mat[x-1][y-1] + 1;
            }
            else {
                mat[x][y] = Math.max(mat[x-1][y], mat[x][y-1]);
            }
        }
    }
    //console.log(mat);
    console.log('lcs length', mat[m][n]);
    
    // backtrack and build the lcs string
    let strLcs = '';
    let i=m,j=n;
    while(i > 0 && j > 0) {
        // if the characters match, move diagnoally
        if ( strA[i-1] === strB[j-1]) {
            strLcs = strA[i-1] + strLcs;
            i--;
            j--;
        }
        // if there's no match, move vertically or horizontally based on max value
        else if (mat[i][j-1] > mat[i-1][j] ) {
            j--;
        }
        else {
            i--;
        }
    }

    console.log(strLcs);
    return strLcs;
}

// tests
lcs("ABAZDC", "BACBAD");
lcs("AGGTAB", "GXTXAYB");
lcs("aaaa", "aa");

