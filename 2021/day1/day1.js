// read from a file
const fs = require("fs")

// getting all the records as a list
const records = fs.readFileSync('input.txt').toString().split('\n')


const part1 = () => {
  let answer = 0

  for(let i=0; i<=records.length-1 ; i++){
    if (parseInt(records[i+1]) > parseInt(records[i])){
      answer++
    }
  }
  console.log(answer)
}

const part2 = () => {
  let answer = 0

  for(let i=0; i<=records.length-1 ; i++){
    if ( parseInt(records[i+1]) + parseInt(records[i+2]) + parseInt(records[i+3]) > parseInt(records[i]) + parseInt(records[i+1]) + parseInt(records[i+2]) ){
      answer++
    }
  }
  console.log(answer)
}

part2()



