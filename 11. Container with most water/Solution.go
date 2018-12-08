package main

import (
	"fmt"
)

func main() {
	nums := []int{1, 8, 6, 2, 5, 4, 8, 3, 7}
	fmt.Println(maxArea(nums))
}

func maxArea(height []int) int {
	i, j := 0, len(height)-1
	max := 0
	for i < j {
		a, b := height[i], height[j]
		h := 0
		l := j - i
		if a < b {
			h = a
			i++
		} else {
			h = b
			j--
		}
		area := h * l
		if area > max {
			max = area
		}

	}
	return max
}
