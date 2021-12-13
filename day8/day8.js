const fs = require('fs')

const linesOutputSignal = fs.readFileSync('input.txt').toString().trim().split('\n').map(line => {
  return line.split(' | ')[1].split(' ')
})

let count = 0
linesOutputSignal.forEach(line => {
  line.forEach(seg => {
    if (seg.length == 2 || seg.length == 4 || seg.length == 3 || seg.length == 7)
      count++
  })
})

console.log(count)
