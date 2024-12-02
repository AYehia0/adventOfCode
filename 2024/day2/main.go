package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

// read the input file and return a slice of strings
func getInput(path string) [][]int {
	file, err := os.Open(path)
	if err != nil {
		fmt.Println("Error reading file")
		os.Exit(1)
	}
	defer file.Close()

	var levels [][]int

	// read the file line by line and split each line by " ", then parse to int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		var level []int
		for _, v := range strings.Split(line, " ") {
			n, _ := strconv.Atoi(v)
			level = append(level, n)
		}
		levels = append(levels, level)
	}

	return levels
}

// checks if the level is valid
// a vaild level is either increasing/decreasing and any 2 adjacent levels differ by at least 1 and at most 3
func check(level []int) bool {

	isIncreasing := func(l []int) bool {
		for i := 1; i < len(l); i++ {
			if l[i] <= l[i-1] {
				return false
			}
		}
		return true
	}

	isDecreasing := func(l []int) bool {
		for i := 1; i < len(l); i++ {
			if l[i] >= l[i-1] {
				return false
			}
		}
		return true
	}

	isAdj := func(l []int) bool {
		for i := 0; i < len(l)-1; i++ {
			if math.Abs(float64(l[i]-l[i+1])) > 3 || l[i]-l[i+1] == 0 {
				return false
			}
		}
		return true
	}

	return (isIncreasing(level) || isDecreasing(level)) && isAdj(level)

}

func part1(levels [][]int) int {
	count := 0
	for _, level := range levels {
		if check(level) {
			count++
		}
	}
	return count
}

func remove(slice []int, i int) []int {
	// Create a new slice with the same elements as the original
	newSlice := make([]int, len(slice))
	copy(newSlice, slice)

	newSlice = append(newSlice[:i], newSlice[i+1:]...)
	return newSlice
}

func part2(levels [][]int) int {
	count := 0

	for _, level := range levels {
		if check(level) {
			count++
		} else {
			for i := 0; i < len(level); i++ {
				newLevel := remove(level, i)
				if check(newLevel) {
					count++
					break
				}
			}
		}
	}
	return count
}

func main() {
	levels := getInput("input.txt")
	fmt.Println("Part 1: ", part1(levels))
	fmt.Println("Part 2: ", part2(levels))
}
