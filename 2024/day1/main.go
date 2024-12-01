package main

import (
	"fmt"
	"math"
	"os"
	"slices"
)

// read the input file and return a slice of strings
func getInput(path string) ([]int, []int) {
	file, err := os.Open(path)
	if err != nil {
		fmt.Println("Error reading file")
		os.Exit(1)
	}
	defer file.Close()

	var a, b int
	var x, y []int
	for {
		_, err := fmt.Fscanf(file, "%d %d\n", &a, &b)
		if err != nil {
			break
		}
		x = append(x, a)
		y = append(y, b)
	}
	return x, y
}

func part1(s1, s2 []int) int {
	ans := 0.0

	slices.Sort(s1)
	slices.Sort(s2)

	for i := 0; i < len(s1); i++ {
		ans += math.Abs(float64(s1[i] - s2[i]))
	}

	return int(ans)
}

func part2(s1, s2 []int) int {
	m := make(map[int]int) // to store the frequency of each element
	ans := 0

	for i := 0; i < len(s1); i++ {
		if _, ok := m[s2[i]]; ok {
			m[s2[i]]++
		} else {
			m[s2[i]] = 1
		}
	}

	for i := 0; i < len(s1); i++ {
		if _, ok := m[s1[i]]; ok {
			ans += s1[i] * m[s1[i]]
		}
	}

	return ans
}

func main() {
	s1, s2 := getInput("input.txt")
	fmt.Println("Part 1: ", part1(s1, s2))
	fmt.Println("Part 2: ", part2(s1, s2))
}
