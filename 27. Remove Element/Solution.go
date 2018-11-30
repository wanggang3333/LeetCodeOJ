package main

import (
	"fmt"
)

func main() {
	nums := []int{1, 2, 3, 3, 2, 4}
	val := 3
	removeElement(nums, val)
	fmt.Println(nums)
}
func removeElement(nums []int, val int) int {
	length := len(nums)
	if length == 0 {
		return 0
	}
	temp := make([]int, 0, length)
	for i := 0; i < length; i++ {
		if nums[i] != val {
			temp = append(temp, i)
		}
	}

	for i := 0; i < len(temp); i++ {
		nums[i] = nums[temp[i]]
	}
	return len(temp)

}
