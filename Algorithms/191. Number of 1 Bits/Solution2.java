//比较巧妙的解法可以将循环次数减少到与1的个数一样。
//利用的性质就是n－1之后，n最低位的1之后（包括其本身）的所有bits翻转。
//http://www.danielbit.com/blog/puzzle/leetcode/leetcode-number-of-1-bits
public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        if(n == 0)
            return 0;
        int i = 0;
        while(n != 0) {
            n = n & (n-1);
            i++;
        }
        return i;
    }
}