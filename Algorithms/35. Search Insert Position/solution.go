package solution

import (
	"fmt"
)

func main() {
	nums := []int{1, 3, 5, 6}
	target := 7
	fmt.Print(searchInsert(nums, target))
}

func searchInsert(nums []int, target int) int {
	for idx, num := range nums {
		if num >= target {
			return idx
		}
	}
	return len(nums)
}
