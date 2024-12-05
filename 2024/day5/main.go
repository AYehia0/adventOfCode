package main

import (
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func getInput(path string) (map[int][]int, [][]int) {
	rules := make(map[int][]int)
	updates := [][]int{}
	contnet, err := os.ReadFile(path)
	if err != nil {
		fmt.Println("Error reading file")
		os.Exit(1)
	}
	sections := strings.Split(strings.TrimSpace(string(contnet)), "\n\n")

	r := sections[0]
	u := sections[1]

	for _, line := range strings.Split(r, "\n") {
		parts := strings.Split(line, "|")
		right, left := parts[0], parts[1]
		rightInt, _ := strconv.Atoi(right)
		leftInt, _ := strconv.Atoi(left)

		// if both numbers are not in the map, add them
		if _, ok := rules[rightInt]; !ok {
			rules[rightInt] = []int{leftInt}
		}

		if _, ok := rules[leftInt]; !ok {
			rules[leftInt] = []int{}
		}

		// if the right number is already in the map, append the left number to it
		if _, ok := rules[rightInt]; ok {
			rules[rightInt] = append(rules[rightInt], leftInt)
		}
	}

	// the updates
	for _, line := range strings.Split(u, "\n") {
		parts := strings.Split(line, ",")

		tmp := []int{}
		for _, part := range parts {
			num, _ := strconv.Atoi(part)
			tmp = append(tmp, num)
		}
		updates = append(updates, tmp)
	}

	return rules, updates
}

func part1(rules map[int][]int, updates [][]int) int {
	ans := 0

	for _, update := range updates {

		// start from the first number in the update
		valid := true
		for i := 1; i < len(update); i++ {
			orderList := rules[update[i]]
			// if the next number is in the order list, break

			if slices.Contains(orderList, update[i-1]) {
				valid = false
				break
			}
		}
		if valid {
			ans += update[len(update)/2]
		}
	}

	return ans
}

func isValidOrder(rules map[int][]int, perm []int) bool {
	for i := 1; i < len(perm); i++ {
		orderList := rules[perm[i]]
		if slices.Contains(orderList, perm[i-1]) {
			return false
		}
	}

	return true
}

func part2(rules map[int][]int, updates [][]int) int {
	ans := 0

	for _, update := range updates {

		// start from the first number in the update
		for i := 1; i < len(update); i++ {
			orderList := rules[update[i]]

			if slices.Contains(orderList, update[i-1]) {
				ordered := []int{}
				remaining := map[int]bool{}
				dependencies := make(map[int][]int)

				for _, num := range update {
					remaining[num] = true

					for _, dep := range rules[num] {
						dependencies[dep] = append(dependencies[dep], num)
					}
				}

				for len(remaining) > 0 {
					for num := range remaining {
						if len(dependencies[num]) == 0 {
							ordered = append(ordered, num)
							delete(remaining, num)

							for k, v := range dependencies {
								newV := []int{}

								for _, dep := range v {
									if dep != num {
										newV = append(newV, dep)
									}
								}
								dependencies[k] = newV
							}

						}
					}
				}

				ans += ordered[len(ordered)/2]
				break
			}
		}
	}

	return ans
}

func main() {
	rules, updates := getInput("input.txt")
	fmt.Printf("Part 1: %d\n", part1(rules, updates))
	fmt.Printf("Part 2: %d\n", part2(rules, updates))
}
