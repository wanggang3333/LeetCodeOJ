package problem0121

func maxProfit(prices []int) int {
	length := len(prices)
	if length <= 1 {
		return 0
	}
	var min int
	var res int
	min = prices[0]
	for i := 1; i < length; i++ {
		temp := prices[i] - min
		if temp > res {
			res = temp
		}
		if prices[i] < min {
			min = prices[i]
		}
	}

	return res
}