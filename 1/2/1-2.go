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

func calc_clicks_and_acc(line []byte, acc int) (int, int) {
	dir_map := map[byte]int{
		'L': -1,
		'R': 1,
	}

	dir := line[0]
	n, err := strconv.Atoi(string(line[1:]))

	if err != nil {
		panic(err)
	}

	prev_acc := acc
	pre_mod_acc := acc + dir_map[dir]*n
	acc = mod(pre_mod_acc, 100)

	var sign_changed int
	if (pre_mod_acc > 0 && prev_acc < 0) || (pre_mod_acc < 0 && prev_acc > 0) {
		sign_changed = 1
	}

	clicks := abs(pre_mod_acc)/100 + sign_changed

	fmt.Printf("prev %d, pre_mod_acc: %d, curr: %d, magnitude: %d, sign_changed: %d, clicks: %d\n", prev_acc, pre_mod_acc, acc, dir_map[dir]*n, sign_changed, clicks)

	return clicks, acc
}

func main() {
	file, err := os.Open("../1-ex.txt")

	if err != nil {
		panic(err)
	}

	scanner := bufio.NewScanner(file)
	acc := 50
	var total_clicks int

	for scanner.Scan() {
		line := scanner.Bytes()

		var new_acc int
		clicks, new_acc := calc_clicks_and_acc(line, acc)
		acc = new_acc

		total_clicks += clicks
	}

	fmt.Printf("Password: %d\n", total_clicks)
}
