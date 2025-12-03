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

func main() {
	dir_map := map[byte]int{
		'L': -1,
		'R': 1,
	}

	file, err := os.Open("1-1.txt")

	if err != nil {
		panic(err)
	}

	scanner := bufio.NewScanner(file)
	acc := 50
	var hits int

	for scanner.Scan() {
		s := scanner.Bytes()
		dir := s[0]
		n, err := strconv.Atoi(string(s[1:]))

		if err != nil {
			panic(err)
		}

		acc = mod((acc + dir_map[dir]*n), 100)

		fmt.Printf("%d\n", acc)

		if acc == 0 {
			hits++
		}
	}

	fmt.Printf("Password: %d\n", hits)
}
