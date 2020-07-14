
// observer pattern

function Subject() {
    // list of listener functions
    this.observers = [];

}


Subject.prototype = {
    subscribe: function(fn) {
        this.observers.push(fn);
    },
    unsubscribe: function(fnToRemove) {
        this.observers = this.observers.filter( fn => fn !== fnToRemove);
    },
    trigger: function(msg) {
        this.observers.forEach( fn => fn(msg));
    }
}


const subject = new Subject();

function observerA(msg) {
    console.log('received by Observer A:', msg);
}

function observerB(msg) {
    console.log('received by Observer B:', msg);
}

subject.subscribe(observerA);
subject.subscribe(observerB);
subject.trigger("hello there");

subject.unsubscribe(observerA);
subject.trigger("done");
