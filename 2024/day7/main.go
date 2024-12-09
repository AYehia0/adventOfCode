package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

// 3267: 81 40 27
// total is 3267
// nums are 81, 40, 27
func getInput(path string) ([]int, [][]int) {
	content, err := os.ReadFile(path)
	if err != nil {
		fmt.Println("Error reading file:", err)
		os.Exit(1)
	}

	totals := []int{}
	numbers := [][]int{}

	for _, line := range strings.Split(strings.TrimSpace(string(content)), "\n") {
		total := strings.Split(line, ": ")[0]
		totalInt, _ := strconv.Atoi(total)
		nums := strings.Split(strings.Split(line, ": ")[1], " ")
		tmp := []int{}
		for _, num := range nums {
			numInt, _ := strconv.Atoi(num)
			tmp = append(tmp, numInt)
		}

		totals = append(totals, totalInt)
		numbers = append(numbers, tmp)
	}

	return totals, numbers
}

func mul(nums []int) int64 {
	var res int64 = 1
	for _, num := range nums {
		res *= int64(num)
	}
	return res
}

// check if a total can be evaluated in order using these operations (* and +)
// example : total=190 and items: 19, 10 ---> 19*10=190 so return true
func checkListEvaluation(total int, items []int) bool {
	// one case if mul of all the items is less than total, it's impossible to get the total
	if mul(items) < int64(total) {
		return false
	}

	// if mul of all the items is equal to total, return true
	if mul(items) == int64(total) {
		return true
	}

	// if mul of all the items is greater than total, check if we can get the total using combinations of + and *
	// example : 3267: 81 40 27 ---> 81 + 40 * 27 and 81 * 40 + 27 both equal 3267
	// trying all the combinations of + and * to get the total

	return false
}

func checkEvalPart1(total int, items []int) bool {
	// Recursive helper function
	var dfs func(current int, remaining []int) bool
	dfs = func(current int, remaining []int) bool {
		if len(remaining) == 0 {
			return current == total
		}

		next := remaining[0]
		newRemaining := remaining[1:]

		if dfs(current+next, newRemaining) {
			return true
		}

		if dfs(current*next, newRemaining) {
			return true
		}

		return false
	}

	if len(items) == 0 {
		return false
	}

	return dfs(items[0], items[1:])
}

func part1(totals []int, nums [][]int) int64 {
	var ans int64

	for i := 0; i < len(totals); i++ {
		tt := totals[i]
		items := nums[i]

		if checkEvalPart1(tt, items) {
			ans += int64(tt)
		}
	}
	return ans
}

func checkEvalPart2(total int, items []int) bool {
	// Recursive helper function
	var dfs func(current int, remaining []int) bool
	dfs = func(current int, remaining []int) bool {
		if len(remaining) == 0 {
			return current == total
		}

		next := remaining[0]
		newRemaining := remaining[1:]

		// 156: 15 6 can be made true through a single concatenation: 15 || 6 = 156
		concat := strconv.Itoa(current) + strconv.Itoa(next)
		concInt, _ := strconv.Atoi(concat)

		if dfs(concInt, newRemaining) {
			return true
		}

		if dfs(current+next, newRemaining) {
			return true
		}

		if dfs(current*next, newRemaining) {
			return true
		}

		return false
	}

	if len(items) == 0 {
		return false
	}

	return dfs(items[0], items[1:])
}

func part2(totals []int, nums [][]int) int64 {
	var ans int64

	for i := 0; i < len(totals); i++ {
		tt := totals[i]
		items := nums[i]

		if checkEvalPart2(tt, items) {
			ans += int64(tt)
		}
	}
	return ans
}

func main() {
	totals, nums := getInput("input.txt")
	fmt.Printf("Part 1: %d\n", part1(totals, nums))
	fmt.Printf("Part 1: %d\n", part2(totals, nums))
}
