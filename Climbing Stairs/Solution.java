public class Solution {
    public int climbStairs(int n) {
        if(n < 3)
            return n;
        int[] count ={1,2};
        int sum = 0;
        for(int i = 3; i <= n; ++i) {
            sum = count[0] + count[1];
            count[0] = count[1];
            count[1] = sum;
        }
        return sum;
    }
}