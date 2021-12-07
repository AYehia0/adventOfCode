// reading the lines 
const fs = require('fs')

// remove the last item : null
const dataLines = fs.readFileSync('input.txt').toString().split('\n').slice(0, -1)

const formatedInputData = dataLines
  .map(line => line.match(/(\d+),(\d+) -> (\d+),(\d+)/).slice(1))
  .map(vals => vals.map(n => parseInt(n)))
  .map(([x1, y1, x2, y2]) => ({x1, y1, x2, y2}))

class Point {
  constructor(x, y) {
    this.x = x
    this.y = y
  }
}

let view = {}
formatedInputData.forEach(item => {

  let {x1, x2, y1, y2} = item

  // checking vert lines 
  if (x1 == x2){
    let minY = Math.min(y1, y2)
    let maxY = Math.max(y1, y2)

    for (let i=minY; i<=maxY; i++){
      // mark it as a point 
      let p = new Point(x1, i)

      p = JSON.stringify(p)
      if (!view[p])
        view[p] = 1
      else {
        view[p]++
      }

    }
  }

  // checking the hor lines 
  else if (y1 == y2) {
    let minX = Math.min(x1, x2)
    let maxX = Math.max(x1, x2)

    for (let i=minX; i<=maxX; i++){
      // mark it as a point 
      let p = new Point(i, y1)

      p = JSON.stringify(p)
      if (!view[p])
        view[p] = 1
      else {
        view[p]++
      }
    }
  }
  // Part 2
  else {
    // calculating the steps 
    let steps = Math.abs(x1 - x2)

    // which direction the point goes 
    let dirX = x2 - x1 > 0 ? 1 : -1
    let dirY = y2 - y1 > 0 ? 1 : -1 

    for (let i=0; i<=steps; i++) {
      p = new Point(x1 + (dirX * i), y1 + (dirY * i))

      p = JSON.stringify(p)
      if (!view[p])
        view[p] = 1
      else {
        view[p]++
      }
  }
  }
})

let ans = 0
for (const [key, value] of Object.entries(view)) {
  if (value > 1)
    ans++
}

console.log(ans)
