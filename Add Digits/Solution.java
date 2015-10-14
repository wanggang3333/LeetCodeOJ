public class Solution {
    public int addDigits(int num) {
        if(num == 0) {
            return 0;
        } else {
            int fac = num % 9;
            if(fac == 0) {
                fac = 9;
            }
            return fac;
        }
    }
}