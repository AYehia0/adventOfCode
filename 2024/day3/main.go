package main

import (
	"fmt"
	"os"
	"regexp"
	"sort"
	"strconv"
)

// read the input file and return a slice of strings
func getInput(path string) string {
	contnet, err := os.ReadFile(path)
	if err != nil {
		fmt.Println("Error reading file")
		os.Exit(1)
	}
	return string(contnet)
}

func part1(input string) int {
	ans := 0
	re := regexp.MustCompile(`mul\(([^(),]+),([^(),]+)\)`)
	for _, match := range re.FindAllStringSubmatch(input, -1) {
		a, b := match[1], match[2]
		aInt, _ := strconv.Atoi(a)
		bInt, _ := strconv.Atoi(b)

		ans += aInt * bInt
	}
	return ans
}

func removeRanges(input string, ranges [][]int) string {
	if len(ranges) == 0 {
		return input
	}

	// Sort ranges by start index to avoid overlap issues
	sort.Slice(ranges, func(i, j int) bool {
		return ranges[i][0] < ranges[j][0]
	})

	result := ""
	lastEnd := 0

	for _, r := range ranges {
		s, e := r[0], r[1]

		if s < lastEnd || s >= len(input) || e > len(input) || s >= e {
			continue
		}

		result += input[lastEnd:s]

		lastEnd = e
	}

	result += input[lastEnd:]

	return result
}

func part2(input string) int {
	ans := 0
	enabled := true

	re := regexp.MustCompile(`(don't\(\)|do\(\)|mul\(([^(),]+),([^(),]+)\))`)
	matches := re.FindAllStringSubmatch(input, -1)

	for _, match := range matches {
		if match[1] == "don't()" {
			enabled = false
		} else if match[1] == "do()" {
			enabled = true
		} else if enabled && match[2] != "" && match[3] != "" {
			a, b := match[2], match[3]
			aInt, _ := strconv.Atoi(a)
			bInt, _ := strconv.Atoi(b)
			ans += aInt * bInt
		}
	}

	return ans
}

func main() {
	input := getInput("input.txt")
	fmt.Printf("Part 1: %d\n", part1(input))
	fmt.Printf("Part 2: %d\n", part2(input))
}
