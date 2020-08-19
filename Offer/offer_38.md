# 面试题38. 字符串的排列
输入一个字符串，打印出该字符串中字符的所有排列。

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

示例:

输入：s = "abc"

输出：["abc","acb","bac","bca","cab","cba"]



限制：

1 <= s 的长度 <= 8





# 面试题38. 字符串的排列
输入一个字符串，打印出该字符串中字符的所有排列。

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

示例:

输入：s = "abc"

输出：["abc","acb","bac","bca","cab","cba"]



限制：

1 <= s 的长度 <= 8

#  面试题38. 字符串的排列  解题思路

```go
func permutation(s string) []string {
    size := len(s)
    if size <= 1 {
        return []string{s}
    }
    res := make([]string, 0)
    used := make([]bool, size)
    m := make(map[string]int)

    helper(s, []byte{}, used, m)

    for k := range m {
        res = append(res, k)
    }
    return res
}

func helper(s string, ans []byte, used []bool, set map[string]int) {
    if len(ans) == len(s) {
        set[string(append([]byte{}, ans...))] = 1
        return
    }
    for i := 0; i < len(s); i++ {
        if used[i] {
            continue
        }
        used[i] = true
        ans = append(ans, s[i])
        helper(s, ans, used, set)
        ans = ans[:len(ans)-1]
        used[i] = false
    }
}

```