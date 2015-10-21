public class Solution {
    public int[] plusOne(int[] digits) {
        int[] ans = new int[digits.length + 1];
        int[] ans2 = new int[digits.length];
        ans[0] = 0;
        int p = digits[digits.length-1] + 1;
        for(int i = 0; i < digits.length; ++i) {
            if(i == digits.length-1) {
                if(p == 10){
                    ans[digits.length-i] = 0;
                    ans[0] = 1;
                } else {
                    ans2[digits.length-1-i] = p;
                }
            }else if(p == 10) {
                ans2[digits.length-1-i] = 0;
                ans[digits.length-i] = 0;
                p = digits[digits.length-2-i] + 1;
            } else {
                ans2[digits.length-1-i] = p;
                ans[digits.length-i] = p;
                p = digits[digits.length-2-i];
            }
        }
        return ans[0]==1 ? ans : ans2;
    }
}