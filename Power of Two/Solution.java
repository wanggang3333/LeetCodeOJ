public class Solution {
    public boolean isPowerOfTwo(int n) {
        if(n <= 0) 
            return false;
        if(n == 1)
            return true;
        while(n % 2 == 0){
            if(n == 2)
                return true;
            n = n / 2;
        }
        return false;
    }
}