const fs = require('fs')

const part1 = () => {

  let count = 0

  const linesOutputSignal = fs.readFileSync('input.txt').toString().trim().split('\n').map(line => {
    return line.split(' | ')[1].split(' ')
  })
  
  linesOutputSignal.forEach(line => {
    line.forEach(seg => {
      if (seg.length == 2 || seg.length == 4 || seg.length == 3 || seg.length == 7)
        count++
    })
  })
  
  return count

}

// helper functions 
// set comparing

function eqSet(s1, s2) {

  let set1 = new Set([...s1])
  let set2 = new Set([...s2])

  if (set1.size !== set2.size) 
    return false
  for (let item of set1) 
    if (!set2.has(item)) 
      return false
    return true
}

// correcting the signals by deduction
const correctSignals = (signals) => {
  
  // checking the unique pattern of signals
  let one = signals.find(signal => signal.length == 2).split('')
  let four = signals.find(signal => signal.length == 4).split('')
  let seven = signals.find(signal => signal.length == 3).split('')
  
  // ONE : 2 segments in one, a must be the one that isn't in se7en
  let a = seven.find(signal => !one.includes(signal))

  // THREE : 
  // there are 3 possible signals : 3, 2 and 5
  let three = signals.find(signal => signal.length == 5).split('')
  console.log(signals.find(signal => {return signal.length == 5}))

  // to get d : in both three and 4 but not in one
  let d = three.find(signal => {
    return !one.includes(signal) && four.includes(signal)
  })

  // to get g : in three but not a or b and not in one
  let g = three.find(signal => {
    return !one.includes(signal) && signal !== a && signal !== d
  })

  // SIX : 
  let six = signals.find(signal => {
    return signal.length == 6 && !one.every(cORf => signal.includes(cORf))
  }).split('')

  // to get c 
  let c = one.find(cORf => !six.includes(cORf))

  // to get f
  let f = one.find(cORf => six.includes(cORf))

  // to get b
  let b = four.find(signal => {
    return !one.includes(signal) && signal !== d
  })

  // finally to get e
  // find all 

  console.log("all segments : ", signals.find(signal => signal.length == 7))
  let allIn = signals.find(signal => signal.length == 7).split('')

  let e = allIn.find(side => {
    return side !== a && side !== b && side !== c && side !== d && side !== f && side !== g
  })

  // output, idk
  // if (e == "e" && g == "g"){
    // e = "g"
    // g = "e"
  // }

  // if (f == "f" && g == "g"){
    // f = "g"
    // g = "f"
  // }

  console.log(`a: ${a}, b: ${b}, c: ${c}, d: ${d}, e: ${e}, f: ${f}, g: ${g}`)
  return {a, b, c, d, e, f, g}
}


const findNums = (correctSignals) => {
 
  const orgNums = ["bacefg", "cf", "acdeg", "acdfg", "bdcf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
  const nums = []

  orgNums.forEach(signal => {
    let splittedSignal = [...signal]

    let numStr = ""
    for (let l of splittedSignal){
      numStr += correctSignals[l]
    }

    // adding 
    nums.push(numStr)
  })

  return nums

}
// decode a it
const decodeSegment = (outSignal, nums) => {
  // 0 --> 9
  for (let ind=0; ind<=nums.length-1; ind++){
    if ([...nums[ind]].every(i => outSignal.includes(i)) && nums[ind].length == outSignal.length){
      console.log(outSignal, nums[ind], ind)
      return ind
    }
  }
}
const part2 = () => {

  let count = 0

  // parsing the data
  const linesOutputSignal = fs.readFileSync('input1.txt').toString().trim().split('\n').map(line => {
    return [line.split(' | ')[0].split(' '), line.split(' | ')[1].split(' ')]
  })

  linesOutputSignal.forEach(line => {

    let signalPatterns = line[0]
    let signalOutputs = line[1]

    console.log('------------------')
    console.log(signalOutputs)
    console.log('------------------')
    // correcting the signals 
    let newCorrectedSignals = correctSignals(signalPatterns)
    let correctNums = findNums(newCorrectedSignals)
    console.log(correctNums)
    console.log('------------------')

    let ans = ""
    for (let out of signalOutputs){
      let x = decodeSegment(out, correctNums)
      ans += x
    }
    count += parseInt(ans)

  })

  console.log(count)
}

part2()
