
// iterate over array and add to heap
function makeHeap(arr) {
    
    const heap = [];
    arr.forEach( a => {
        heap.push(a);
        heapify(heap, heap.length-1);
    });

    return heap;
}

// maintain head properties as elements are added
function heapify(heap, index) {
    
    if(index <= 0 ) {   
        return;
    }

    // bubble up
    const pid = Math.floor((index - 1)/2);

    // swap elements
    if(heap[pid] > heap[index]) {
        let temp = heap[index];
        heap[index] = heap[pid];
        heap[pid] = temp;
    }

    return heapify(heap, pid);
}

const input = [4, 10, 3, 5, 1];
const maxHeapOutput = [10, 5, 3, 4, 1];
const minHeapOutput = [1, 3, 4, 10, 5];

console.log(makeHeap(input));
