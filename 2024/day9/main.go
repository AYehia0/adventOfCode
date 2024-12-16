package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func getInput(path string) string {
	content, err := os.ReadFile(path)
	if err != nil {
		fmt.Println("Error reading file:", err)
		os.Exit(1)
	}
	c := strings.TrimSpace(string(content))
	return c

	// return strings.Split(c, "")
}

func part1(input string) int {
	m := []rune{}
	isBlock := true
	fileId := 0
	ans := 0

	for _, numRune := range input {
		num, _ := strconv.Atoi(string(numRune))

		if isBlock {
			for i := 0; i < num; i++ {
				m = append(m, rune('0'+fileId))
			}
			fileId++
		} else {
			for i := 0; i < num; i++ {
				m = append(m, '.')
			}
		}
		isBlock = !isBlock
	}

	l, r := 0, len(m)-1
	for l < r {
		if m[l] != '.' {
			l++
		} else if m[r] == '.' {
			r--
		} else {
			m[l] = m[r]
			m[r] = '.'
			l++
			r--
		}
	}

	id := 0

	for m[id] != '.' {
		ans += id * int(m[id]-'0')
		id++
	}

	return ans
}

func main() {
	m := getInput("input.txt")
	fmt.Println("Part 1:", part1(m))
}
