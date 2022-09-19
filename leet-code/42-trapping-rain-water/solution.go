package main

import "fmt"

func main() {
	// result := trap([]int{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1})
	result := trap([]int{4, 2, 0, 3, 2, 5})
	fmt.Println(result)
}

func trap(height []int) int {

	result := 0
	legs := []int{}

	for index, value := range height {
		// ensure minimum size
		for value > len(legs)-1 {
			legs = append(legs, 0)
		}

		// check old
		for i := 0; i <= value; i++ {
			result += legs[i]
			legs[i] = 0
		}

		// advance
		for i := value + 1; i < len(legs); i++ {
			legs[i] += 1
		}

		fmt.Println(index, result)
	}

	return result
}
