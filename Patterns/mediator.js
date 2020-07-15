

// mediator pattern
// example of a chatroom mediating interaction between members

function Member(name) {
    this.name = name;
    this.chatroom = null;
}

Member.prototype = {
    send: function(message, toMemeber) {
        this.chatroom.send(message, this, toMemeber);
    },
    receive: function(message, fromMember) {
        console.log('rec:',fromMember.name,' -> ', this.name, ':', message);
    }
}

function Chatroom() {
    this.members = {};
}

Chatroom.prototype = {
    addMember: function(member) {
        this.members[member.name] = member;
        member.chatroom = this;
    },
    send: function(message, fromMember, toMemeber) {
        if (this.members[toMemeber]) {
            this.members[toMemeber].receive(message, fromMember);
        }
    }
}

const chat = new Chatroom();

const alpha = new Member('Alpha');
const beta = new Member('Beta');
const gamma = new Member('Gamma');
const pika = new Member('Pika');

chat.addMember(alpha);
chat.addMember(beta);
chat.addMember(gamma);

alpha.send("Hello there", "Beta");
gamma.send("What's up", "Alpha");
beta.send("What's up", "Pika");

