
// visitor pattern

function Players(name, score) {
    this.name = name;
    this.score = score;
}

Players.prototype = {
    getScore: function() {  
        return this.score; 
    },
    setScore: function(newScore) { 
        this.score = newScore; 
    },
    accept: function(visitorFn) {
        visitorFn(this);
    }
}

const alpha = new Players("Alpha", 1000);
const beta = new Players("Beta", 1500);

console.log(alpha.getScore());

// create a visitor function and pass it to base
function bonusScore(player) {
    player.setScore(player.getScore() * 2);
}

alpha.accept(bonusScore);

console.log(alpha.getScore());
