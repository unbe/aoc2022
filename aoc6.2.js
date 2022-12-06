var fs = require('fs');
var data = fs.readFileSync(0, 'utf-8');
var sync = data.substr(0, 14)
for(var i = 14; i < data.length; i++) {
  sync = (sync + data[i]).substr(1);
  if(new Set(sync).size == 14) {
    console.log(i + 1);
    break;
  }
}
