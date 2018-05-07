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
  var ppc = inputs.slice(1,n+1).map( x => parseInt(x,10));
  var noc = inputs.slice(n+1,inputs.length).map( x => parseInt(x,10));
  var sum = maxProd(ppc,noc);
  console.log(sum);
}

function maxProd(ppc,noc) {
  ppc.sort((a,b) => a- b);
  noc.sort((a,b) => a- b);

  var sum = 0;
  ppc.forEach( (x,i) => {
    sum += (x * noc[i]);
  });
  return sum;

}
