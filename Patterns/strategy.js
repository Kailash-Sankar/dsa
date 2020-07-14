
// strategy pattern


function Alpha() {
    this.price = item => {
        return 1250;
    }
}

function Beta() {
    this.price = item => {
        return 1210;
    }
}

function Gamma() {
    this.price = item => {
        return 2120;
    }
}

const alpha = new Alpha();
const beta = new Beta();
const gamma = new Gamma();

// we can be encapsualted the strategies in a wrapper
// and change strategies without affecting the usage interface

function Sellers() {
    this.company = "";

    this.setStrategy = (company) => {
        this.company = company;
    }

    this.price = item => {
        return this.company.price(item);
    }
}


const sellers =  new Sellers();

sellers.setStrategy(alpha);
console.log(sellers.price("keyboard"));


sellers.setStrategy(beta);
console.log(sellers.price("keyboard"));

sellers.setStrategy(gamma);
console.log(sellers.price("keyboard"));

