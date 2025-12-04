package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func mod(a, b int) int {
	return (a%b + b) % b
}

func abs(n int) int {
	if n >= 0 {
		return n
	}
	return -n
}

func main() {
	file, err := os.Open("../1.txt")

	if err != nil {
		panic(err)
	}

	scanner := bufio.NewScanner(file)
	acc := 50
	var total_clicks int

	for scanner.Scan() {
		line := scanner.Bytes()

		dir_map := map[byte]int{
			'L': -1,
			'R': 1,
		}

		dir := dir_map[line[0]]
		n, err := strconv.Atoi(string(line[1:]))

		if err != nil {
			panic(err)
		}

		var clicks int

		for range abs(n) {
			acc = mod(acc+dir, 100)
			if acc == 0 {
				clicks++
			}
		}
		total_clicks += clicks
	}

	fmt.Printf("Password: %d\n", total_clicks)
}
