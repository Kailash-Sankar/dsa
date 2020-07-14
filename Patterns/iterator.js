
// iterator pattern

const items = [1,"a","hello", true];

function Iterator(items) {
    this.items = items;
    this.index = 0;
}

// forward iterator
Iterator.prototype = {
    hasNext: function() {
        console.log('hasNext', this);
        return this.index < this.items.length;
    },

    next: function() {
        return this.items[this.index++];
    }
}

const iter = new Iterator(items);

while(iter.hasNext()) {
    console.log(iter.next());
}


