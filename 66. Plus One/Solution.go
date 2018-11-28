package  problem0066

func plusOne(digits []int) []int {
    length := len(digits)
    if length == 0 {
        return []int{1}
    }
    
    digits[length-1]++
    for i := length -1; i > 0; i-- {
        if digits[i] >= 10 {
            digits[i] -= 10
            digits[i-1]++
        }
    }
    if digits[0] >= 10 {
        digits[0] -= 10
        digits = append([]int{1},digits...)
    }
    return digits
}

