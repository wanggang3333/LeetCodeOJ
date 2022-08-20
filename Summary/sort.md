<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>
# 排序算法

| 排序算法   | 时间复杂度（最好/平均/最坏）     | 空间复杂度 | 稳定性 |
| ---------- | -------------------------------- | ---------- | ------ |
| 冒泡排序   | $$O(n)/O(n^2)/O(n^2)$$           | O(1)       | 稳定   |
| 选择排序   | $$O(n^2)/O(n^2)/O(n^2)$$         | O(1)       | 不稳定 |
| 插入排序   | $$O(n)/O(n^2)/O(n^2)$$           | O(1)       | 稳定   |
| 希尔排序   | $$O(n)/O(n^{1.3})/O(n^2)$$       | O(1)       | 不稳定 |
| 归并排序   | $$O(nlogn)/O(nlogn)/O(nlogn)$$   | O(n)       | 稳定   |
| 快速排序   | $$O(n^2)/O(nlogn)/O(nlogn)$$     | O(nlogn)   | 不稳定 |
| 堆排序     | $$O(nlogn)/O(nlog_2n)/O(nlogn)$$ | O(1)       | 不稳定 |
| 非比较排序 |
| 计数排序   | $$O(n+k)/O(n+k)/O(n+k)$$         | O(n+k)     | 稳定   |
| 桶排序     | $$O(n^2)/O(n+k)/O(n+k)$$         | O(n+k)     | 稳定   |
| 基数排序   | $$O(n*k)/O(n*k)/O(n*k)$$         | O(n+k)     | 稳定   |

## 冒泡排序

```go
func BubbleSort(data []int) {
    length := len(data)
    for i := 0; i < length-1; i++ {
        for j := 0; j < len-1-i; j++ {
            if data[j] > data[j+1] {
                data[j], data[j+1] = data[j+1], data[j]
            }
        }
    }   
}
```

## 选择排序

```go
func SelectSort(data []int) {
    length := len(data)
    var minIdx int
    for i := 0; i < length-1; i++ {
        minIdx = i
        for j := i+1; j < len; j++ {
            if data[j] < data[minIdx] {
                minIdx = j
            }
        }
        data[i], data[minIdx] = data[minIdx], data[i]
    }   
}

```

## 插入排序

```go
func InsertSort(data []int) {
    length := len(data)
    var preIdx, current int
    for i := 1; i < length; i++ {
        preIdx = i-1
        current = data[i]
        for preIdx >= 0 && data[preIdx] >current {
            data[preIdx+1] = data[preIdx]
            preIdx = preIdx - 1
        }
        data[preIdx+1] = current
    }   
}

```

## 希尔排序

```go
func ShellSort(data []int) {
	length := len(data)
	for gap := int(math.Floor(float64(length / 2))); gap > 0; gap = int(math.Floor(float64(gap / 2))) {
		for i:= gap; i < length; i++ {
			j := i
			current := data[i]
			for j -gap >= 0 && current < data[j-gap] {
				data[j] = data[j-gap]
				j = j - gap
			}
			data[j] = current
		}
	}
}

```

## 归并排序

```go
func MergeSort(data []int) []int {
	length := len(data)
	if length < 2 {
		return data
	}
	mid := length / 2
	return merge(MergeSort(data[:mid]), MergeSort(data[mid:]))
}

func merge(left, right []int) []int {
	leftLen := len(left)
	rigLen := len(right)
	result := make([]int, 0, leftLen+rigLen)
	i := 0
	j := 0
	for i < leftLen && j < rigLen {
		if left[i] < right[j] {
			result = append(result, left[i])
			i = i + 1
		} else {
			result = append(result, right[j])
			j = j + 1
		}
	}
	if i < leftLen {
		result = append(result, left[i:]...)
	}
	if j < rigLen {
		result = append(result, right[j:]...)
	}
	return result
}

```

## 快速排序

```go
func QuickSort(data []int) {
	quickSort(data, 0, len(data)-1)
}

func quickSort(data []int, left, right int) {
	if left < right {
		partitionIdx := partition(data, left, right)
		quickSort(data, left, partitionIdx-1)
		quickSort(data, partitionIdx+1, right)
	}
}

func partition(data []int, left, right int) int {
	pivot := left
	idx := pivot + 1
	for i := idx; i <= right; i++ {
		if data[i] < data[pivot] {
			data[i], data[idx] = data[idx], data[i]
			idx += 1
		}
	}
	data[pivot], data[idx-1] = data[idx-1], data[pivot]
	return idx - 1
}
```

## 堆排序

```go
// Heap 定义堆排序过程中使用的堆结构
type Heap struct {
    arr  []int   // 用来存储堆的数据
    size int     // 用来标识堆的大小
}

// adjustHeap 用于调整堆，保持堆的固有性质
func adjustHeap(h Heap, parentNode int) {
    leftNode := parentNode*2 + 1
    rightNode := parentNode*2 + 2

    maxNode := parentNode
    if leftNode < h.size && h.arr[maxNode] < h.arr[leftNode] {
        maxNode = leftNode
    }
    if rightNode < h.size && h.arr[maxNode] < h.arr[rightNode] {
        maxNode = rightNode
    }

    if maxNode != parentNode {
        h.arr[maxNode], h.arr[parentNode] = h.arr[parentNode], h.arr[maxNode]
        adjustHeap(h, maxNode)
    }
}

// createHeap 用于构造一个堆
func createHeap(arr []int) (h Heap) {
    h.arr = arr
    h.size = len(arr)

    for i := h.size / 2; i >= 0; i-- {
        adjustHeap(h, i)
    }
    return
}

// heapSort 使用堆对数组进行排序
func heapSort(arr []int) {
    h := createHeap(arr)

    for h.size > 0 {
        // 将最大的数值调整到堆的末尾
        h.arr[0], h.arr[h.size-1] = h.arr[h.size-1], h.arr[0]
        // 减少堆的长度
        h.size--
        // 由于堆顶元素改变了，而且堆的大小改变了，需要重新调整堆，维持堆的性质
        adjustHeap(h, 0)
    }
}   
```