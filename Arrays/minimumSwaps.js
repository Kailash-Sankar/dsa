

// minimum swaps required to sort an array
// 4 3 1 2 => 3
// 7, 1, 3, 2, 4, 5, 6 => 5
function minimumSwaps(arr) {

    // maintain element to it's current position mapping
    const arrPos = arr.map( (x,i) => ([x,i]) );
    arrPos.sort( (a,b) => a[0] - b[0] );

    let swaps = 0;
    const visited = new Set();
    arrPos.forEach( (ele, idx) => {
        // correct position
        if(visited.has(idx) || ele[1] == idx ) {
            return;
        }

        // count cycles
        let pos = ele[1]
        let cycleSize = 0
        while(!visited.has(pos)) {
            visited.add(pos);
            pos = arrPos[pos][1]
            cycleSize++;
        }

        if(cycleSize > 0) {
            swaps = swaps + (cycleSize-1);
        }

    });

    return swaps;
}
