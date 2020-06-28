
// merge an array of multiple meeting time ranges 
// and returns an array of condensed ranges
// time values are indicated by integers (x 30min shift from 9:30 am)
function mergeRanges(meetings) {

  // sort by startTime asc
  const sortedMeetings = [...meetings].sort(
    (a,b) => a.startTime - b.startTime
  );
  
  // start with the first meeting
  // handle exceptions if there no meetings
  const mergedMeetings = [sortedMeetings[0]];
  
  for(let i=1; i< sortedMeetings.length; i++) {
    const currentMeeting = sortedMeetings[i];
    const recentMeeting = mergedMeetings[mergedMeetings.length - 1];
  
    // if the current meeting is outside of the most recent meeting
    // push it to the merged list
    if (currentMeeting.startTime > recentMeeting.endTime) {
      mergedMeetings.push({...currentMeeting});
    }  
    // if it's within range, merge the meetings
    // starTime will be the start of the previous one
    // endTime will be the max value amoung the two
    else {
      recentMeeting.endTime = Math.max(recentMeeting.endTime, currentMeeting.endTime);
    }
  }
  return mergedMeetings;
}


// Tests

let desc = 'meetings overlap';
let actual = mergeRanges([{ startTime: 1, endTime: 3 }, { startTime: 2, endTime: 4 }]);
let expected = [{ startTime: 1, endTime: 4 }];
assertArrayEquals(actual, expected, desc);

desc = 'meetings touch';
actual = mergeRanges([{ startTime: 5, endTime: 6 }, { startTime: 6, endTime: 8 }]);
expected = [{ startTime: 5, endTime: 8 }];
assertArrayEquals(actual, expected, desc);

desc = 'meeting contains other meeting';
actual = mergeRanges([{ startTime: 1, endTime: 8 }, { startTime: 2, endTime: 5 }]);
expected = [{ startTime: 1, endTime: 8 }];
assertArrayEquals(actual, expected, desc);

desc = 'meetings stay separate';
actual = mergeRanges([{ startTime: 1, endTime: 3 }, { startTime: 4, endTime: 8 }]);
expected = [{ startTime: 1, endTime: 3 }, { startTime: 4, endTime: 8 }];
assertArrayEquals(actual, expected, desc);

desc = 'multiple merged meetings';
actual = mergeRanges([
  { startTime: 1, endTime: 4 },
  { startTime: 2, endTime: 5 },
  { startTime: 5, endTime: 8 },
]);
expected = [{ startTime: 1, endTime: 8 }];
assertArrayEquals(actual, expected, desc);

desc = 'meetings not sorted';
actual = mergeRanges([
  { startTime: 5, endTime: 8 },
  { startTime: 1, endTime: 4 },
  { startTime: 6, endTime: 8 },
]);
expected = [{ startTime: 1, endTime: 4 }, { startTime: 5, endTime: 8 }];
assertArrayEquals(actual, expected, desc);

desc = 'oneLongMeetingContainsSmallerMeetings';
actual = mergeRanges([
  { startTime: 1, endTime: 10 },
  { startTime: 2, endTime: 5 },
  { startTime: 6, endTime: 8 },
  { startTime: 9, endTime: 10 },
  { startTime: 10, endTime: 12 }
]);
expected = [
  { startTime: 1, endTime: 12 }
];
assertArrayEquals(actual, expected, desc);

desc = 'sample input';
actual = mergeRanges([
  { startTime: 0, endTime: 1 },
  { startTime: 3, endTime: 5 },
  { startTime: 4, endTime: 8 },
  { startTime: 10, endTime: 12 },
  { startTime: 9, endTime: 10 },
]);
expected = [
  { startTime: 0, endTime: 1 },
  { startTime: 3, endTime: 8 },
  { startTime: 9, endTime: 12 },
];
assertArrayEquals(actual, expected, desc);

function assertArrayEquals(a, b, desc) {
  // Sort the keys in each meeting to avoid
  // failing based on differences in key order.
  orderedA = a.map( function(meeting) {
    return JSON.stringify(meeting, Object.keys(meeting).sort());
  });
  orderedB = b.map( function(meeting) {
    return JSON.stringify(meeting, Object.keys(meeting).sort());
  });
  const arrayA = JSON.stringify(orderedA);
  const arrayB = JSON.stringify(orderedB);
  if (arrayA !== arrayB) {
    console.log(`${desc} ... FAIL: ${JSON.stringify(a)} != ${JSON.stringify(b)}`)
  } else {
    console.log(`${desc} ... PASS`);
  }
}
