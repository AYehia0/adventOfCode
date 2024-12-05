package main

import (
	"fmt"
	"os"
	"strings"
)

func getInput(path string) []string {
	contnet, err := os.ReadFile(path)
	if err != nil {
		fmt.Println("Error reading file")
		os.Exit(1)
	}
	lines := strings.Split(strings.TrimSpace(string(contnet)), "\n")
	return lines
}

// the basic solution is to find where the X starts then trace to the rest (MAS) in all directions (up, up-left, up-right, down, down-left, down-right, right, left)
func part1(lines []string) int {
	ans := 0
	grid := make([][]rune, len(lines))
	targetWord := "XMAS"

	for i, line := range lines {
		grid[i] = []rune(line)
	}

	// (x, y)
	directions := [][2]int{
		{0, 1},  // up
		{0, -1}, // down
		{1, 0},  // right
		{-1, 0}, // left

		{1, 1},  // up-right
		{1, -1}, // up-left

		{-1, 1},  // down-right
		{-1, -1}, // down-left
	}

	for r := 0; r < len(grid); r++ {
		for c := 0; c < len(grid[r]); c++ {
			if grid[r][c] != 'X' {
				continue
			}
			for _, dir := range directions {
				dr, dc := dir[0], dir[1]
				found := true

				for i := 0; i < len(targetWord); i++ {
					r2, c2 := r+dr*i, c+dc*i

					if r2 < 0 || r2 >= len(grid) || c2 < 0 || c2 >= len(grid[r]) {
						found = false
						break
					}

					if grid[r2][c2] != rune(targetWord[i]) {
						found = false
						break
					}
				}

				if found {
					ans++
				}
			}
		}
	}
	return ans
}

// here it's MAS in X shape, so we need to check in diagonal directions only (up-right, up-left, down-right, down-left) and reverse too
func part2(lines []string) int {
	ans := 0
	grid := make([][]rune, len(lines))

	for i, line := range lines {
		grid[i] = []rune(line)
	}

	directions := [][][2]int{
		// diagonal 1
		{
			{1, 1},   // up-right
			{-1, -1}, // down-left

		},
		// diagonal 2
		{
			{1, -1}, // up-left
			{-1, 1}, // down-right
		},
	}

	for r := 0; r < len(grid); r++ {
		for c := 0; c < len(grid[r]); c++ {
			if grid[r][c] != 'A' {
				continue
			}
			found := true

			for _, dirs := range directions {

				r1, c1 := r+dirs[0][0], c+dirs[0][1]
				r2, c2 := r+dirs[1][0], c+dirs[1][1]

				if r1 < 0 || r1 >= len(grid) || c1 < 0 || c1 >= len(grid[r]) || r2 < 0 || r2 >= len(grid) || c2 < 0 || c2 >= len(grid[r]) {
					found = false
					break
				}

				if (grid[r1][c1] == 'M' && grid[r2][c2] == 'S') || (grid[r1][c1] == 'S' && grid[r2][c2] == 'M') {
					continue
				}

				found = false
				break
			}

			if found {
				ans++
			}
		}
	}

	return ans
}

func main() {
	grid := getInput("input.txt")
	fmt.Printf("Part1: %d\n", part1(grid))
	fmt.Printf("Part2: %d\n", part2(grid))
}
