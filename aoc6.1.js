var fs = require('fs');
var data = fs.readFileSync(0, 'utf-8');
var sync = data.substr(0, 4)
for(var i = 4; i < data.length; i++) {
  sync = (sync + data[i]).substr(1);
  if(new Set(sync).size == 4) {
    console.log(i + 1);
    break;
  }
}
