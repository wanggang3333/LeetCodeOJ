package gokit

import "fmt"

// Stack 用于存放int的栈
type Stack struct {
	nums []int
}

// NewStack NewStack
func NewStack() *Stack {
	return &Stack{nums: []int{}}
}

// Push Push
func (s *Stack) Push(n int) {
	s.nums = append(s.nums, n)
}

// Pop Pop
func (s *Stack) Pop() int {
	if s.Len() == 0 {
		msg := fmt.Sprintf("Stack length is zero, can not pop")
		panic(msg)
	}
	res := s.nums[s.Len()-1]
	s.nums = s.nums[0:s.Len()-1]
	return res
}

// Len 栈的长度
func (s *Stack) Len() int {
	return len(s.nums)
}

// IsEmpty 是否为空
func (s *Stack) IsEmpty() bool {
	return s.Len() == 0
}
