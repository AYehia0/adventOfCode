const fs = require('fs')

const data = fs.readFileSync('input.txt').toString().split(',').map(n => { return parseInt(n) })

const maxPos = Math.max(...data)

const part1 = () => {
  // largest possible fuel
  let largestFuel = Number.MAX_VALUE
  
  for(let i=0; i<maxPos; i++) {
  
    let fuel = 0
  
    // trying all possible tries
    for (const pos of data){
      // each step costs 1
      fuel += Math.abs(pos - i)
    }
  
    // checking if the fuel is bigger than the current fuel
    if (fuel < largestFuel)
      largestFuel = fuel
  
  }
  return largestFuel

}

const part2 = () => {
  // largest possible fuel
  let largestFuel = Number.MAX_VALUE
  
  for(let i=0; i<maxPos; i++) {
  
    let fuel = 0
  
    // trying all possible tries
    for (const pos of data){
      // to find step cost : 1 -> 5  would be (5-1)=4 1+2+3+4 == 10
      // one way to solve it by : n * (n+1)/2  (4*5)/2
      let steps = Math.abs(pos - i)
      fuel += (steps* (steps+1))/2
    }
  
    // checking if the fuel is bigger than the current fuel
    if (fuel < largestFuel)
      largestFuel = fuel
  
  }
  return largestFuel

}

console.log(part2())
