 
 // Write a function that takes an integer flightLength (in minutes) 
 // and an array of integers movieLengths (in minutes) 
 // and returns a boolean indicating whether there are two numbers in movieLengths 
 // whose sum equals flightLength.
 
 // Determine if two movie runtimes add up to the flight length
function canTwoMoviesFillFlight(movieLengths, flightLength) {
  const movieSet = new Set();

   for(let i=0; i < movieLengths.length; i++) {
    const movie = movieLengths[i];
    const diff = flightLength - movie;
    
    // match found
    if (movieSet.has(diff)) {
      return true;
    }
    
    // add visited values to set
    movieSet.add(movie);
  }

  return false;
}


// Tests

let desc = 'short flight';
let actual = canTwoMoviesFillFlight([2, 4], 1);
let expected = false;
assertEquals(actual, expected, desc);

desc = 'long flight';
actual = canTwoMoviesFillFlight([2, 4], 6);
expected = true;
assertEquals(actual, expected, desc);

desc = 'one movie half flight length';
actual = canTwoMoviesFillFlight([3, 8], 6);
expected = false;
assertEquals(actual, expected, desc);

desc = 'two movies half flight length';
actual = canTwoMoviesFillFlight([3, 8, 3], 6);
expected = true;
assertEquals(actual, expected, desc);

desc = 'lots of possible pairs';
actual = canTwoMoviesFillFlight([1, 2, 3, 4, 5, 6], 7);
expected = true;
assertEquals(actual, expected, desc);

desc = 'not using first movie';
actual = canTwoMoviesFillFlight([4, 3, 2], 5);
expected = true;
assertEquals(actual, expected, desc);

desc = 'only one movie';
actual = canTwoMoviesFillFlight([6], 6);
expected = false;
assertEquals(actual, expected, desc);

desc = 'no movies';
actual = canTwoMoviesFillFlight([], 2);
expected = false;
assertEquals(actual, expected, desc);

function assertEquals(a, b, desc) {
  if (a === b) {
    console.log(`${desc} ... PASS`);
  } else {
    console.log(`${desc} ... FAIL: ${a} != ${b}`);
  }
}


// same problem extended for three movies
function canThreeMoviesFillFlight(movieLengths, flightLength) {
  const movieSet = new Set();
  
  
  for(let j=0; j< movieLengths.length-1; j++) {
    const movieOne = movieLengths[j];
    
    for(let i=j+1; i < movieLengths.length; i++) {
      const movie = movieLengths[i];
      const diff = flightLength - movieOne - movie;
    
      // match found
      if (movieSet.has(diff)) {
        return true;
      }
    
      // add visited values to set
      movieSet.add(movie);
    }
  }

  return false;
}

desc = 'three movies: quick test #1';
actual = canThreeMoviesFillFlight([1, 2, 3, 4, 5, 6], 7);
expected = true;
assertEquals(actual, expected, desc);

desc = 'three movies: quick test #2';
actual = canThreeMoviesFillFlight([1, 8, 3, 4, 5, 12], 7);
expected = false;
assertEquals(actual, expected, desc);
