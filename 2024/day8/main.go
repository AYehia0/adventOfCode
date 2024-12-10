package main

import (
	"fmt"
	"os"
	"strings"
)

func getInput(path string) (map[string][][2]int, int, int) {
	gridMap := map[string][][2]int{}
	content, err := os.ReadFile(path)
	if err != nil {
		fmt.Println("Error reading file:", err)
		os.Exit(1)
	}
	grid := strings.Split(strings.TrimSpace(string(content)), "\n")
	gridWidth := len(grid[0])
	gridHeight := len(grid)
	for i, line := range grid {
		for j, char := range strings.Split(line, "") {

			if char == "." {
				continue
			}

			// add the char to the gridMap if it doesn't exist
			if _, ok := gridMap[char]; !ok {
				gridMap[char] = [][2]int{{i, j}}
			} else {
				gridMap[char] = append(gridMap[char], [2]int{i, j})
			}
		}
	}

	return gridMap, gridWidth, gridHeight
}

func isTwiceAsFar(pos1, pos2, antinode [2]int) bool {
	d1 := abs(pos1[0]-antinode[0]) + abs(pos1[1]-antinode[1])
	d2 := abs(pos2[0]-antinode[0]) + abs(pos2[1]-antinode[1])
	return d1 == 2*d2 || d2 == 2*d1
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func isWithinBounds(pos [2]int, width, height int) bool {
	return pos[0] >= 0 && pos[0] < height && pos[1] >= 0 && pos[1] < width
}

func part1(grid map[string][][2]int, width, height int) int {
	visited := map[[2]int]bool{}

	for _, positions := range grid {
		for i := 0; i < len(positions); i++ {
			for j := i + 1; j < len(positions); j++ {
				pos1 := positions[i]
				pos2 := positions[j]

				// Calculate the vector between the two points
				dx := pos2[1] - pos1[1]
				dy := pos2[0] - pos1[0]

				// Calculate the two antinode positions
				antinode1 := [2]int{pos1[0] - dy, pos1[1] - dx}
				antinode2 := [2]int{pos2[0] + dy, pos2[1] + dx}

				// if the antinode x and y doesn't exceed the grid boundaries add it
				if isWithinBounds(antinode1, width, height) && isTwiceAsFar(pos1, pos2, antinode1) {
					visited[antinode1] = true
				}

				if isWithinBounds(antinode2, width, height) && isTwiceAsFar(pos2, pos1, antinode2) {
					visited[antinode2] = true
				}
			}
		}
	}

	return len(visited)
}

func part2(grid map[string][][2]int, width, height int) int {
	visited := map[[2]int]bool{}

	// Add all antenna positions to visited
	for _, positions := range grid {
		for _, pos := range positions {
			visited[pos] = true
		}
	}

	// Process each pair of antennas for each frequency
	for _, positions := range grid {
		for i := 0; i < len(positions); i++ {
			for j := i + 1; j < len(positions); j++ {
				pos1 := positions[i]
				pos2 := positions[j]

				// Calculate the vector between the two points
				dx := pos2[1] - pos1[1]
				dy := pos2[0] - pos1[0]

				// Add antinodes along the line
				for k := 1; ; k++ {
					antinode1 := [2]int{pos1[0] - k*dy, pos1[1] - k*dx}
					antinode2 := [2]int{pos2[0] + k*dy, pos2[1] + k*dx}

					// Break if both antinodes are out of bounds
					if !isWithinBounds(antinode1, width, height) && !isWithinBounds(antinode2, width, height) {
						break
					}

					// Add valid antinodes to visited
					if isWithinBounds(antinode1, width, height) {
						visited[antinode1] = true
					}
					if isWithinBounds(antinode2, width, height) {
						visited[antinode2] = true
					}
				}
			}
		}
	}

	return len(visited)
}

func main() {
	grid, w, h := getInput("input.txt")
	fmt.Printf("Part 1: %d\n", part1(grid, w, h))
	fmt.Printf("Part 2: %d\n", part2(grid, w, h))
}
