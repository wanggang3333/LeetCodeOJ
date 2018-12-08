public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        for(int i = 0; i < 16; ++i) {
            n = switchBits(n, i, 32 - 1 - i);
        }
        return n;
    }
    
    public int switchBits(int n, int i, int j) {
        int a = (n >> i) & 1;
        int b = (n >> j) & 1;
        
        if((a ^ b) != 0) {
            n ^= (1<<i) | (1<<j);
        }
        return n;
    }
}