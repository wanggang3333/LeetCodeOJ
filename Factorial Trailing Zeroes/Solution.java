public class Solution {
    public int trailingZeroes(int n) {
        if(n < 0)
            return -1;
            
        int count = 0;
        long i = 5;
        while(i <= n) {
            count += n / i;
            i *= 5;
        }
        return count;
    }
}