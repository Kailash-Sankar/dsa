
// proxy pattern

function CrptoApi() {
    this.getValue = function(coin) {
        console.log('calling api', coin);
        switch(coin) {
            case 'Bitcoin':
                    return "1000";
            case 'Litecoin':
                    return "1234";
            case 'Etherium':
                    return "523";
        }
    }
}

// create a proxy to use the api service
// proxy adds additional functionality
// to a similar interface
function CryptoProxy() {
    this.api = new CrptoApi();
    this.cache = {};

    this.getValue = (coin) => {
        if (!(coin in this.cache)) {
            console.log(this.cache);
            this.cache[coin] = this.api.getValue(coin);
        }
        return this.cache[coin];
    }

}

const proxy = new CryptoProxy();
console.log(proxy.getValue("Bitcoin"));
console.log(proxy.getValue("Etherium"));
console.log(proxy.getValue("Bitcoin"));
console.log(proxy.getValue("Bitcoin"));
console.log(proxy.getValue("Bitcoin"));
console.log(proxy.getValue("Litecoin"));
