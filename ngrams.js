var natural = require('natural')
var tokenizer = new natural.WordTokenizer()
var fs = require('fs')

var file = fs.readFile('us_lowercasesubs.txt', 'utf8', function (err, data) {
  if (err) console.log('err')
  console.log(data)
})
