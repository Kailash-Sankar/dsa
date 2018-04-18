// Classification standards
var groups = {
  private_discovered : [
    { base : '0xc0a8ffff' , key:'192.168.x.x' },
    { base : '0x0affffff', key:'10.x.x.x' },
    { base : '0xac1fffff', key: '172.[16-31].x.x' }
  ],
  multi_cast : [
    { base : '0xe00000ff', key : 'Local_Network_Control_Block'}, //224.0.0.0 - 224.0.0.255 (/24) Local Network Control Block
    { base : '0xe00001ff', key: 'Internetwork_Control_Block'}, //224.0.1.0 - 224.0.1.255 (/24) Internetwork Control Block
    { base : '0xe000ffff', key : 'AD-HOC_Block_I' }, //224.0.2.0 - 224.0.255.255 (65024) AD-HOC Block I
    { base : '0xe001ffff', key: 'Reserved'}, //224.1.0.0 - 224.1.255.255 (/16) RESERVED
    { base : '0xe002ffff', key: 'SDP/SAP_Block'}, //224.2.0.0 - 224.2.255.255 (/16) SDP/SAP Block
  ]
};

// global list for output
// initlizie to avoid comparison during ip classification
var buckets = { 'public_unknown_discovered' : {} };
Object.keys(groups).forEach( function(k) { buckets[k] = {}; })

// return ip after converting to hex
function hexify(ip) {
  var hex ='0x';
  // iterate, convert to hex, prepend zero if required
  ip.split('.').forEach( (oct) => {
    var base = Number(oct).toString(16);
    hex += base.length < 2 ? '0'+base : base;
  });
  return hex;
}

// Accept an ip, apply it against standard classes and put it in a bucket
function groupIP(ip) {
  var _ip = hexify(ip);
  // Apply group by group
  for ( var l1 in groups ) {
    // iterate on each rule in a group
    for(var i=0,n=groups[l1].length;i<n;i++) {
      var grp = groups[l1][i];
      if ( (grp.base | ~_ip) == -1 )  {
        //console.log(ip,'fits in',l1);
        bucketThis(l1,grp.key,ip);
        return; // found the bucket for our ip
      }
    } // end for - rule in a group
  } // end for - groups

  //if we reach here then the ip did not match any of the rules
  // so after DNS logic, whatever remains becomes classified on /8 mask
  _ip = _ip.slice(0,4); // 0x + first octet
  bucketThis('public_unknown_discovered',_ip,ip);
}

function bucketThis(l1,l2,ip) {
  if ( buckets[l1].hasOwnProperty(l2) ) {
    buckets[l1][l2].push(ip);
  }
  else {
    buckets[l1][l2] = [ip];
  }
}


// test
var ip_list = ['192.168.1.42','172.21.1.42','172.16.12.42','172.34.1.4','224.0.1.22','224.0.0.22','224.0.22.22','224.1.2.21','224.2.31.255'];
ip_list.forEach( function(ip){ groupIP(ip); });
console.log('output',buckets);
