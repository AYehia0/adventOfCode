package main

import (
	"fmt"
	"os"
	"strings"
)

type ItemLocation struct {
	item string
}

func getInput(path string) []string {
	content, err := os.ReadFile(path)
	if err != nil {
		fmt.Println("Error reading file:", err)
		os.Exit(1)
	}
	return strings.Split(strings.TrimSpace(string(content)), "\n")
}

func makeGrid(lines []string) (map[[2]int]ItemLocation, [2]int, int, int) {
	grid := map[[2]int]ItemLocation{}
	start := [2]int{0, 0}

	for i, line := range lines {
		for j, char := range strings.Split(line, "") {
			if char == "^" {
				start = [2]int{i, j}
			}
			grid[[2]int{i, j}] = ItemLocation{
				item: char,
			}
		}
	}

	return grid, start, len(lines[0]), len(lines)
}

func part1(grid map[[2]int]ItemLocation, start [2]int, width, height int) int {
	// Directions: [Up, Right, Down, Left]
	directions := [][2]int{
		{-1, 0}, // Up
		{0, 1},  // Right
		{1, 0},  // Down
		{0, -1}, // Left
	}

	visited := map[[2]int]bool{}
	currPos := start
	dirIndex := 0

	for {
		visited[currPos] = true

		nextPos := [2]int{
			currPos[0] + directions[dirIndex][0],
			currPos[1] + directions[dirIndex][1],
		}

		if nextPos[0] < 0 || nextPos[0] >= height || nextPos[1] < 0 || nextPos[1] >= width {
			break
		}

		nextLoc := grid[nextPos]
		if nextLoc.item == "#" {
			// Obstacle; turn right
			dirIndex = (dirIndex + 1) % 4
		} else {
			currPos = nextPos
		}
	}

	return len(visited)
}

func isStuckInLoop(grid map[[2]int]ItemLocation, start [2]int, width, height int) bool {
	// Directions: [Up, Right, Down, Left]
	directions := [][2]int{
		{-1, 0}, // Up
		{0, 1},  // Right
		{1, 0},  // Down
		{0, -1}, // Left
	}

	visitedStates := map[[3]int]bool{} // Tracks (row, col, dirIndex)
	currPos := start
	dirIndex := 0

	for {
		// Mark current state
		state := [3]int{currPos[0], currPos[1], dirIndex}
		if visitedStates[state] {
			// Loop detected
			return true
		}
		visitedStates[state] = true

		// Calculate the next position
		nextPos := [2]int{
			currPos[0] + directions[dirIndex][0],
			currPos[1] + directions[dirIndex][1],
		}

		// Check if the guard is leaving the grid
		if nextPos[0] < 0 || nextPos[0] >= height || nextPos[1] < 0 || nextPos[1] >= width {
			return false
		}

		// Check the next position
		nextLoc := grid[nextPos]
		if nextLoc.item == "#" {
			// Obstacle; turn right
			dirIndex = (dirIndex + 1) % 4
		} else {
			// Move to the next position
			currPos = nextPos
		}
	}
}

func part2(grid map[[2]int]ItemLocation, start [2]int, width, height int) int {
	validPositions := 0

	// Iterate over all positions in the grid
	for row := 0; row < height; row++ {
		for col := 0; col < width; col++ {
			pos := [2]int{row, col}

			// Skip if it's not an empty space or is the guard's starting position
			if grid[pos].item != "." || pos == start {
				continue
			}

			// Place a temporary obstruction
			grid[pos] = ItemLocation{item: "#"}

			// Check if it causes a loop
			if isStuckInLoop(grid, start, width, height) {
				validPositions++
			}

			// Remove the obstruction
			grid[pos] = ItemLocation{item: "."}
		}
	}

	return validPositions
}

func main() {
	lines := getInput("input_test.txt")
	grid, start, width, height := makeGrid(lines)
	fmt.Printf("Part1: %d\n", part1(grid, start, width, height))
	fmt.Printf("Part2: %d\n", part2(grid, start, width, height))
}
