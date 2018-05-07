var readline = require('readline');

process.stdin.setEncoding('utf8');
var rl = readline.createInterface({
  input: process.stdin,
  terminal: false
});

var lines='';
rl.on('line', readLine);
rl.on('close',main);

function  readLine(line) {
  if (line !== "\n") {
    if(lines) lines+=' ';
    lines+=line;
  }
}

function main() {
  //console.log(lines);
  var inputs = lines.toString().split(' ');
  //console.log(inputs);
  var n = parseInt(inputs[0], 10);
  var ar = inputs.slice(1,n+1).map( x => parseInt(x,10));
  var found = findMajority(n,ar);
  console.log(found);
}

function findMajority(n,ar) {
  var item = {}, s = n/2;

  for(var i=0; i<n; i++) {
    var vote = ar[i];
    if ( item.hasOwnProperty(vote) ) { item[vote]++; }
    else { item[vote] = 1; }

    if ( i > s && item[vote] > s ) { return 1; }
  }
  return 0;
}
