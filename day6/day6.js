const fs = require('fs')
// reading the input

const fishes = fs.readFileSync('input.txt').toString().split(',').map(n => {return parseInt(n)})

const days = 80
let totalFishes = 0

for (let day=0; day<days; day++) {

  for (let i=fishes.length; i>=0; i--){

    if (fishes[i] > 0){
      fishes[i]--
    }
    // reset
    // change it back to 6 and add another fish of life 
    else if (fishes[i] == 0){
      fishes[i] = 6
      fishes.push(8)
    }
  }
}

console.log(fishes.length)

