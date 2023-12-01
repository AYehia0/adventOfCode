package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func ReadFileIntoSlice(path string) []string {
	lines := []string{}

	file, err := os.Open(path)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, strings.TrimSpace(scanner.Text()))
	}

	return lines
}

func part1(lines []string) int {

	ans := 0
	for _, line := range lines {
		tmp := ""
		if line != "" {
			re := regexp.MustCompile("[0-9]")
			matches := re.FindAllString(line, -1)
			if len(matches) == 1 {
				tmp += matches[0]
				tmp += matches[0]
			} else {
				tmp += matches[0]
				tmp += matches[len(matches)-1]
			}
			i, err := strconv.Atoi(tmp)
			if err != nil {
				log.Fatalf("Error: %v", err)
			}
			ans += i
		}
	}
	return ans
}
func calculateNumericValue(word string) string {
	wordValues := map[string]string{
		"one":   "1",
		"two":   "2",
		"three": "3",
		"four":  "4",
		"five":  "5",
		"six":   "6",
		"seven": "7",
		"eight": "8",
		"nine":  "9",
	}

	return wordValues[word]
}

// meh way to trick it
func replaceWords(input string) string {
	replacements := map[string]string{
		"twone":     "twoone",
		"oneight":   "oneeight",
		"threeight": "threeeight",
		"fiveight":  "fiveeight",
		"sevenine":  "sevennine",
		"eightwo":   "eighttwo",
		"eighthree": "eightthree",
	}

	result := input
	for old, new := range replacements {
		result = strings.Replace(result, old, new, -1)
	}

	return result
}

func part2(lines []string) int {
	ans := 0
	re := regexp.MustCompile("(one|two|three|four|five|six|seven|eight|nine|\\d)")
	for _, line := range lines {
		tmp := ""
		if line != "" {
			matches := re.FindAllString(replaceWords(line), -1)
			l1 := matches[0]
			l2 := matches[len(matches)-1]

			if len(l1) > 1 {
				tmp += calculateNumericValue(l1)
			} else {
				tmp += l1
			}

			if len(l2) > 1 {
				tmp += calculateNumericValue(l2)
			} else {
				tmp += l2
			}

			i, err := strconv.Atoi(tmp)
			if err != nil {
				log.Fatalf("Error: %v", err)
			}
			fmt.Println(line, l1, l2)
			ans += i
		}
	}
	return ans
}

func main() {
	filename := "./input.txt"
	lines := ReadFileIntoSlice(filename)
	fmt.Printf("Answer P1: %d\n", part1(lines))
	fmt.Printf("Answer P2: %d\n", part2(lines))
}
