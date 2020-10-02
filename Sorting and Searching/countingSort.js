
// sort scores in O(n)
// where highestPossibleScore is a constant of value 100
// counting sort

function sortScores(unorderedScores, highestPossibleScore) {
  const sortedScores = [];

  // Sort the scores in O(n) time
  const scoreIndex = Array(highestPossibleScore+1).fill(0); 
  for(let i=0; i<=highestPossibleScore;i++) {
    scoreIndex[unorderedScores[i]]+=1;
  }
  
  for(let j=highestPossibleScore; j>0;j--) {
    if(scoreIndex[j] > 0) {
      sortedScores.push(...Array(scoreIndex[j]).fill(j));
    }
  }
  return sortedScores;
}


// Tests

let desc = 'no scores';
let actual = sortScores([], 100);
let expected = [];
assertEqual(JSON.stringify(actual), JSON.stringify(expected), desc);

desc = 'one score';
actual = sortScores([55], 100);
expected = [55];
assertEqual(JSON.stringify(actual), JSON.stringify(expected), desc);

desc = 'two scores';
actual = sortScores([30, 60], 100);
expected = [60, 30];
assertEqual(JSON.stringify(actual), JSON.stringify(expected), desc);

desc = 'many scores';
actual = sortScores([37, 89, 41, 65, 91, 53], 100);
expected = [91, 89, 65, 53, 41, 37];
assertEqual(JSON.stringify(actual), JSON.stringify(expected), desc);

desc = 'repeated scores';
actual = sortScores([20, 10, 30, 30, 10, 20], 100);
expected = [30, 30, 20, 20, 10, 10];
assertEqual(JSON.stringify(actual), JSON.stringify(expected), desc);

function assertEqual(a, b, desc) {
  if (a === b) {
    console.log(`${desc} ... PASS`);
  } else {
    console.log(`${desc} ... FAIL: ${a} != ${b}`);
  }
}
