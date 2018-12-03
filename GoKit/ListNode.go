package gokit

import (
	"fmt"
)

//ListNode 链表节点
type ListNode struct {
	Val int
	Next *ListNode
}

//List2Ints convert List to []int
func List2Ints(head *ListNode) []int {
	limit := 100
	
	times := 0
	
	res := []int{}
	for head != nil {
		times++
		if times > limit {
			msg := fmt.Sprintf("链条深度超过%d，可能出现环状链条。请检查错误，或者放宽 l2s 函数中 limit 的限制。", limit)
			panic(msg)
		}

		res = append(res, head.Val)
		head = head.Next
	}
	return res
}

//Ints2List convert []int to List
func Ints2List(nums []int) *ListNode {
	if len(nums) == 0 {
		return nil
	}
	res := &ListNode{
		Val: nums[0],
	}

	temp := res
	for i := 1; i < len(nums); i++ {
		temp.Next = &ListNode{
			Val:nums[i],
		}
		temp = temp.Next
	}
	return res
}

