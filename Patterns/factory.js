
// a simple example of the factory pattern

function xbox(model) {
    this.model = model;
    this.type = "XBOX";
    this.specs = {};
}

function playstation(model) {
    this.model = model;
    this.type = "PlayStation";
    this.specs = {};
}

function wii(model) {
    this.model = model;
    this.type = "Wii";
    this.specs = {};
}


function ConsoleFactory() {
    this.create = (model, type) => {
        switch(type) {
            case 1:
                return new xbox(model);
            case 2:
                return new playstation(model);
            case 3:
                return new wii(model);
        }
    }
}

const consoleBuilder = new ConsoleFactory();

const console = [];

console.push(consoleBuilder.create("360", 1));
console.push(consoleBuilder.create("4", 2));
console.push(consoleBuilder.create("One", 1));
console.push(consoleBuilder.create("3", 2));
console.push(consoleBuilder.create("U", 3));

function ShowConsole() {
    console.log(`Console Type ${this.type}, Model: ${this.model}`);
}


console.forEach( c => ShowConsole.call(c));
