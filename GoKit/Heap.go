package gokit

/* 	堆总是满足下列性质：
	堆中某个节点的值总是不大于或不小于其父节点的值
	堆总是一棵完全二叉树
container/heap 接口定义
type Interface interface {
	sort.Interface
	Push(x interface{}) // add x as element Len()
	Pop() interface{}   // remove and return element Len() - 1.
}
*/

type intHeap []int

func (h intHeap) Len() int {
	return len(h)
}

func (h intHeap) Less(i, j int) bool {
	return h[i] < h[j]
}

func (h intHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *intHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *intHeap) Pop() interface{} {
	res := (*h)[h.Len()-1]
	*h = (*h)[:h.Len()-1]
	return res
}
