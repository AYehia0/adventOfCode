const fs = require('fs')

// reading the input file
const records = fs.readFileSync('input.txt').toString().split('\n')

// first thing 
const part1 = () => {
  let forward = 0
  let up = 0
  let down = 0

  for(let i=0; i<= records.length-1; i++){
    let command = records[i].split(' ')[0]
    let dist = parseInt(records[i].split(' ')[1])

    if (command == 'forward')
      forward+=dist

    if (command == 'up')
      up+=dist

    if (command == 'down')
      down+=dist

    console.log(forward, up, down)
  }

  console.log(forward*(down-up))
}

// part 2 waoh
const part2 = () => {
  let aim = 0
  let forward = 0
  let up = 0
  let down = 0

  for(let i=0; i<= records.length-1; i++){
    let command = records[i].split(' ')[0]
    let dist = parseInt(records[i].split(' ')[1])

    if (command == 'forward'){
      forward+=dist
      down += aim*dist
    }

    if (command == 'up'){
      aim-=dist
    }

    if (command == 'down'){
      aim+=dist
    }

    console.log(forward, up, down)
  }

  console.log(forward*(down-up))
}


part2()
