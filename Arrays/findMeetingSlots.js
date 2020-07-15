
// find free meeting slots between two input calender slots
// there will also be an upper and lower time bound for each user
// a duration will also be provided

// brute approach
// - convert time slots in to comparable format
// - find upper and lower bound from each of the individual bounds
// - combine the individual meetings lists in to one while preserving sort order (meeting start time)
// - condense/merge overlapping meeting windows to get the list of all slots which cannot be used
// - iterate from lower bound to upper bound (increment by duration) and check if it's a free slot

// NOTE: all corner cases are not covered

// compare/convert time actions, abstracted
function compareTime(t1, t2) {
    return t1 > t2;
}

function convertToMins(time) {
    const [h,m] = time.split(':').map(x => parseInt(x,10));
    return (h*60) + m;
}

const converter =  x => [convertToMins(x[0]), convertToMins(x[1])];

const getTimeFromMins = (m) => {
    const hours = Math.floor(m/60);
    const minutes = m%60;
    return hours.toString().padStart(2,'0') + ':' + minutes.toString().padStart(2,'0');
}

const revertConversion = ([x,y]) => [getTimeFromMins(x), getTimeFromMins(y)];


// combine meetings in start order in to one list
function mergeMeetings(p1, p2) {
    const combinedMeetings = [];
    let i=0, j=0;

    while(i + j < (p1.length + p2.length)) {
        // left overs
        if ( i >= p1.length) {
            combinedMeetings.push(p2[j]);
            j++;
            continue;
        }

        if ( j >= p2.length) {
            combinedMeetings.push(p1[i]);
            i++;
            continue;
        }

        // check and push
        if( p1[i][0] < p2[j][0]) {
            combinedMeetings.push(p1[i]);
            i++;
        }
        else {
            combinedMeetings.push(p2[j]);
            j++;
        }
    }
    return combinedMeetings;
}

// merge meeting windows together to get all occupied slots
function condenseMeetings(allMeetings) {
    const condensedMeetings = [allMeetings[0]];
    for(let i=1; i<allMeetings.length; i++) {
        const recent =   condensedMeetings[condensedMeetings.length - 1];
        const current = allMeetings[i];

        // if the endtime of the most recent meeting is within the start time of the current one
        // then combine in to one occupied slot
        if( recent[1] >= current[0] ) {
            recent[1] = Math.max(recent[1], current[1]); // max end time
        }
        else {
            condensedMeetings.push(current);
        }
    } 
    return condensedMeetings;
}

// wrapper
function findSlots(p1, p1Bound, p2, p2Bound, duration) {
    const lowerBound = convertToMins(compareTime(p1Bound[0], p2Bound[0]) ? p1Bound[0] : p2Bound[0]);
    const upperBound = convertToMins(compareTime(p1Bound[1], p2Bound[1]) ? p2Bound[1] : p1Bound[1]);

    console.log(lowerBound, upperBound);

    const parsedP1 = p1.map(converter);
    const parsedP2 = p2.map(converter);

    // combine meetings ordered by start times
    const allMeetings = mergeMeetings(parsedP1, parsedP2);
    console.log(allMeetings);

    // condense the slots
    const condensedMeetings = condenseMeetings(allMeetings);
    console.log(condensedMeetings);

    // find open slots
    const availableSlots = [];
    let idx = 0;
    for(let start=lowerBound; start <= upperBound - duration; start=start+duration) {
        let end = start + duration;

        if(checkOverlap([start, end], condensedMeetings)) {
            continue;
        }

        availableSlots.push([start, end]);
    }
    console.log(availableSlots);

    return availableSlots.map(revertConversion);
}


// check for overlapping time slows
function checkOverlap(time, slots) {
    // no slots
    if (slots.length === 0) {
        return false;
    }

    // end time less than slot one
    if( time[1] <= slots[0][0]) {
        return false;
    }

    // start time after last slot
    if ( time[0] >= slots[slots.length-1][1] ) {
        return false;
    }

    // check if start or end time overlaps a blocked window
    let state = false;
    for(let i=0; i<slots.length; i++) {
        if( slots[i][0] <= time[0] && time[0] < slots[i][1] ) {
            state = true;
        }

        if( slots[i][0] < time[1] && time[1] <= slots[i][1] ) {
            state = true;
        }
    }
    return state;
}


// test
const p1 = [ ["09:00","10:30"], ["12:00", "13:00"], ["16:00","18:00"] ];
const p1Bound = ["9:00", "20:00"];

const p2 = [ ["10:00","11:30"], ["12:30", "14:30"], ["14:30","15:00"], ["16:00", "17:00"] ];
const p2Bound = ["10:00", "18:30"];

const duration = 30;

const availableSlots = findSlots(p1, p1Bound, p2, p2Bound, duration);
console.log(availableSlots);
// output: [["11:30","12:00"], ["15:00", "16:00"], ["18:00","18:30"]]

