public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        if(n == 0)
            return 0;
        int i = 0;
        for(int j = 0; j < 32; ++j) {
            i += n & 1;
            n = n>>1;
        }
        return i;
    }
}