// count the number of islands
// nearby 1's indicate one island

const mat = [
    [1, 1, 0, 0, 0], 
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1],
];
/*
0 0 0
0 1 0
0 0 0

 i-1,j-1    i-1,j   i-1,j+1
 i,j-1      i,j     i,j+1
 i+1,j-1    i+1,j   i+1,j+1
*/

const visited = new Set();

const getKey = (i,j) => `${i}-${j}`;

function findNeighbours(i, j) { 
    const neighbours = [
        [i-1,j-1], [i-1,j], [i-1,j+1],
        [i,j-1], [i,j], [i,j+1],
        [i+1,j-1], [i+1,j], [i+1,j+1]
    ];
    return neighbours.filter( item => (item[0] >= 0 && item[0] < mat.length) && (item[1] >=0 && item[1] < mat[0].length));
}

//console.log(findNeighbours(0,0))

function checkNode(i, j) {
    const key = getKey(i, j);
    if(visited.has(key)) { return false; }
    visited.add(key);
    
    const neighbours = findNeighbours(i,j);
    //console.log(neighbours);
    for(let x=0; x<neighbours.length;x++) {
        const [nI,nJ] = neighbours[x];
        //console.log(nI, nJ);
        if(mat[nI][nJ] === 1) { 
            checkNode(nI, nJ); 
        }
        else {
            visited.add(getKey(i,j));
        }
    }
    return true;
}

let islandCount = 0;
for(let i=0;i<mat.length; i++) {
    const row = mat[i];
    for(let j=0;j< row.length; j++) {
        if(mat[i][j] === 1 && checkNode(i,j)) {
            islandCount++;
        }
    }
}

console.log('Islands', islandCount);
