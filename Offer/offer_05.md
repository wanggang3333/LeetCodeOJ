# 面试题05. 替换空格

请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."



限制：`0 <= s 的长度 <= 10000`

# 面试题05.解题思路

遍历输入字符串, 使用[]rune保存结果

```
func replaceSpace(s string) string {
    res := make([]rune, 0, len(s)*3)
    for _, si := range s {
        if si == ' '{
            res = append(res, '%', '2', '0')
        } else {
            res = append(res, si)
        }
    }

    return string(res)
}
```