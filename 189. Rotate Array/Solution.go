package main

import (
	"fmt"
)

func main() {
	nums := []int{1,2,3,4,5,6,7}
	k := 3
	rotate(nums,k)
	fmt.Print(nums)
}
func rotate(nums []int, k int)  {
	length := len(nums)
	if length <= 1 || k == 0 {
		return
	}

	if k > length {
		k = k % length
	}

	reverse := func (i int, j int)	{
		for i < j {
			nums[i], nums[j] = nums[j], nums[i]
			i++
			j--
		}
	}

	reverse(0,length-1)
	reverse(0,k-1)
	reverse(k,length-1)
	return
}