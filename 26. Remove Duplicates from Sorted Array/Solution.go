package main

import (
	"fmt"
)

func main() {
	nums := []int{0, 0, 1, 1, 1, 2, 2, 3, 3, 4}
	length := removeDuplicates(nums)
	fmt.Println(nums[:length])
}
func removeDuplicates(nums []int) int {
	length := len(nums)
	if length == 0 {
		return 0
	}

	idx := 0
	for i := 1; i < length; i++ {
		if nums[i] != nums[idx] {
			idx++
			nums[idx] = nums[i]
		}
	}
	return idx + 1
}
