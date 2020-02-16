package problem0283

func moveZeroes(nums []int)  {
	length := len(nums)
	if length <= 1 {
		return
	}
	var curr int
	var nozeroInx int
	for curr = 0; curr < length; curr++ {
		if nums[curr] != 0 {
			nums[nozeroInx] = nums[curr]
			nozeroInx++
		}
	}

	for nozeroInx < length {
		nums[nozeroInx] = 0
		nozeroInx++
	}
	return
}