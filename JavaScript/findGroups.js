var input = [
    { "parent": 1, "children": [ 2 ] },
    { "parent": 2, "children": [ 1 ] },
    { "parent": 3, "children": [ 7 ] },
    { "parent": 4, "children": [ 5, 6 ] },
    { "parent": 5, "children": [ 4, 6, 7 ] },
    { "parent": 6, "children": [ 4, 5 ] },
    { "parent": 7, "children": [ 3, 5 ] },
    { "parent": 8, "children": [ 9 ] },
    { "parent": 9, "children": [ 8, 11 ] },
    { "parent": 10, "children": [ 11, 12 ] },
    { "parent": 11, "children": [ 9, 10 ] },
    { "parent": 12, "children": [ 10 ] }
];

/* expected output
var groups = [
    [1, 2],
    [3, 4, 5, 6, 7],
    [8, 9, 10, 11, 12]
];
*/

// navie approach
function findGropsA(elements) {
  const out = {};
  const groups = {};
  idx = 0;

  elements.forEach( e => {
    const items = [e.parent, ...e.children];
    let gid = items.reduce( (gid=idx, x) => {
      gid = groups[x] || gid;
      return gid;
    });
    gid = gid || ++idx;
    items.forEach( y => {
      groups[y] = gid;
    });
  });

  for( let [k,v] of Object.entries(groups) ) { 
    if ( v in out) { out[v].push(k);}
    else { out[v] = [k]; }
  }
  
  return Object.values(out);
}

// using a depth firt style
function findGropsB(elements) {
  const eleMap = {};
  elements.forEach( e => {
    eleMap[e.parent] = e.children;
  });

  const groups = [];
  const visited = {};

  Object.keys(eleMap).forEach( k => {
    let grp = [];
    let stk = [k];
    while( stk.length > 0) {
      let x = stk.pop();
      if (!(x in visited)) {
        grp.push(x);
        visited[x] = true;
        stk = stk.concat(eleMap[x]);
      }
    }
    grp.length && groups.push(grp);
  });

  return groups;
}

 console.log('resultA', findGropsA(input));
 console.log('resultB', findGropsB(input));


