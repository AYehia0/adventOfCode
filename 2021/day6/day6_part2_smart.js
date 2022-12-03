const fs = require('fs')

let fishes = fs.readFileSync('input.txt').toString().split(',').map(n => {return parseInt(n)})

let fishesHolder = [0,0,0,0,0,0,0,0,0]
const days = 256

// one linear array
fishes.forEach(fish => {
  fishesHolder[fish]++
})

// calculating the fishes
for (let day=0; day<days; day++) {
  console.log(fishesHolder)
  fishesHolder[(day+7)%9] += fishesHolder[day%9]
}
console.log(fishesHolder.reduce((a, b) => a + b, 0))
