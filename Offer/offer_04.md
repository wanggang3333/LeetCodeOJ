# [面试题04. 二维数组中的查找](https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/)

在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。



示例:

现有矩阵 matrix 如下：
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
给定 target = 5，返回 true。

给定 target = 20，返回 false。



限制：
```
0 <= n <= 1000

0 <= m <= 1000
```





# 面试题04. 二维数组中的查找

解法一：利用数组规律

Go：从左下角开始找，利用递增关系，大于往右边找，小于往上找，超出返回false

--执行用时：40ms--消耗内存：6.3MB

```
func findNumberIn2DArray(matrix [][]int, target int) bool {
    //以左下角为原点
    i:=len(matrix)-1//获取右下角y坐标
    j:=0//获取右下角x坐标
    for i>-1{
        if j<len(matrix[i]){
            if target<matrix[i][j]{
                i--  //小于target,向上查找
            }else if target>matrix[i][j]{
                j++ //大于targat,向右查找
            }else if target==matrix[i][j]{
                return true
            }
        }else{
            return false//超出数组返回false
        }
    }
    return false//超出matrix返回false
}
```

解法二：利用sort包下的SeachInts方法

Go：因为数组已经是递增关系，利用sort包下的SeachInts方法，遍历数组切片，查找数组中是否含有target值，如果查找不到，返回值是target应该插入数组的位置（会保持数组的递增顺序），此时需要分情况：
情况1：返回值=len(a)，即插入后长度+1，说明target数组内不存在。
情况2：返回值<len(a)，此时不能认为target在数组内，因为返回的是“插入后保持递增顺序的位置“，所以必须将target与数组中该位置的值进行比较，相同才返回true。

--执行用时：32ms--消耗内存：6.3MB
```
func findNumberIn2DArray(matrix [][]int, target int) bool {
    for _,nums:=range matrix{
        i:=sort.SearchInts(nums,target)
        if i<len(nums)&&target==nums[i]{
            return true
        }
    }
    return false
}

```