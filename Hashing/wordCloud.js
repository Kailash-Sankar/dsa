// build a world cloud
// count words in a sentance

const breaks = [' ','.',',',':','?','!'];
const ignoreList = ['-'];

const capitalize = (word) => word.charAt(0).toUpperCase() + word.slice(1);

// assume that an upper case word is counted as upper case only if
// it exists in upper case form across the whole string

class WordCloudData {
  constructor(inputString) {
    this.wordsToCounts = new Map();
    this.populateWordsToCounts(inputString);
  }

  populateWordsToCounts(inputString) {
    let startIndex = null;
    let wordLength = 0;
    // Count the frequency of each word
    for(let i=0; i<=inputString.length;i++) {
      const c = inputString[i];
      
      // check for word breaking character
      // handle last word
      if(breaks.includes(c) || i === inputString.length) {
        let word = inputString.slice(startIndex, startIndex + wordLength);
        let baseCount = this.wordsToCounts.get(word) || 0;
        
        // ignore special cases
        if(ignoreList.includes(word) || wordLength === 0) { wordLength = 0; continue; }
        
        // lower case word
        // if upper case exists, delete key and add count to lowercase
        if( word === word.toLowerCase()) {
          const upWord = capitalize(word);
          const upCount = this.wordsToCounts.get(upWord) || 0;
          if(upCount) {
            baseCount = baseCount + upCount;
            this.wordsToCounts.delete(upWord);
          }
        }
        // upper case word
        // if lower case exists already, then increment it
        else {
          const lowWord = word.toLowerCase();
          const lowCount = this.wordsToCounts.get(lowWord) || 0;
          if(lowCount) {
            word = lowWord;
            baseCount = baseCount + lowCount;
          }
        }
        
        // add to map  
        this.wordsToCounts.set(word,baseCount + 1);
        wordLength = 0;
      }
      else {
        if(wordLength === 0) {
          startIndex = i;
        }
        wordLength = wordLength + 1;
      }
    }
    
  }
}


// Tests

// There are lots of valid solutions for this one. You
// might have to edit some of these tests if you made
// different design decisions in your solution.


let desc = 'simple sentence';
let actual = new WordCloudData('I like cake').wordsToCounts;
let expected = new Map([['I', 1], ['like', 1], ['cake', 1]]);
assert(isMapsEqual(actual, expected), desc);

desc = 'longer sentence';
actual = new WordCloudData('Chocolate cake for dinner and pound cake for dessert').wordsToCounts;
expected = new Map([['and', 1], ['pound', 1], ['for', 2], ['dessert', 1],
  ['Chocolate', 1], ['dinner', 1], ['cake', 2]]);
assert(isMapsEqual(actual, expected), desc);

desc = 'punctuation';
actual = new WordCloudData('Strawberry short cake? Yum!').wordsToCounts;
expected = new Map([['cake', 1], ['Strawberry', 1], ['short', 1], ['Yum', 1]]);
assert(isMapsEqual(actual, expected), desc);

desc = 'hyphenated Words';
actual = new WordCloudData('Dessert - mille-feuille cake').wordsToCounts;
expected = new Map([['cake', 1], ['Dessert', 1], ['mille-feuille', 1]]);
assert(isMapsEqual(actual, expected), desc);

desc = 'ellipses between words';
actual = new WordCloudData('Mmm...mmm...decisions...decisions').wordsToCounts;
expected = new Map([['mmm', 2], ['decisions', 2]]);
assert(isMapsEqual(actual, expected), desc);
/*
desc = 'apostrophes';
actual = new WordCloudData("Allie's Bakery: Sasha's Cakes").wordsToCounts;
expected = new Map([['Bakery', 1], ['Cakes', 1], ["Allie's", 1], ["Sasha's", 1]]);
assert(isMapsEqual(actual, expected), desc);
*/

function isMapsEqual(map1, map2) {
  if (map1.size !== map2.size) {
    return false;
  }
  for (let [key, val] of map1) {
    const testVal = map2.get(key);

    // In cases of an undefined value, make sure the key
    // actually exists on the object so there are no false positives
    if (testVal !== val || (testVal === undefined && !map2.has(key))) {
      return false;
    }
  }
  return true;
}

function assert(condition, desc) {
  if (condition) {
    console.log(`${desc} ... PASS`);
  } else {
    console.log(`${desc} ... FAIL`);
  }
}
