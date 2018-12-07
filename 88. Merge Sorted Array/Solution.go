package main

import (
	"fmt"
)

func main() {
	m := []int{1, 2, 3, 0, 0, 0}
	n := []int{2, 5, 6}
	merge(m, 3, n, 3)
	fmt.Println(m)
}

func merge(nums1 []int, m int, nums2 []int, n int) {
	if n == 0 {
		return
	}

	if m == 0 {
		for i := 0; i < n; i++ {
			nums1[i] = nums2[i]
		}
		return
	}

	tempNum1 := []int{}
	tempNum1 = append(tempNum1, nums1[0:m]...)

	i := 0
	j := 0
	k := 0

	for i < m && j < n {
		if tempNum1[i] < nums2[j] {
			nums1[k] = tempNum1[i]
			i++
		} else {
			nums1[k] = nums2[j]
			j++
		}
		k++
	}
	if i == m {
		for j < n {
			nums1[k] = nums2[j]
			k++
			j++
		}
	}
	if j == n {
		for i < m {
			nums1[k] = tempNum1[i]
			k++
			i++
		}
	}
}
