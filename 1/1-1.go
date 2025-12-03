package main

import (
	"fmt"
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

	s := "L22"

	var acc int

	rs := []byte(s)
	dir := rs[0]
	n, err := strconv.Atoi(string(rs[1:]))

	if err != nil {
		panic(err)
	}

	acc = mod((acc + dir_map[dir]*n), 100)

	fmt.Printf("%d\n", acc)
}
