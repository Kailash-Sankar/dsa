// write the sum(1)(2)(3)...(n)() function
// it should return sum of all inputs


// a crude yet simple approach
let s = 0;
function sum(x) {    
    if(isNaN(x)) {
        return s;
    }
    s += x;
    return y => sum(y);
}

const x = sum(1)(2)(3)(4)(0)(5)();

console.log(x);
