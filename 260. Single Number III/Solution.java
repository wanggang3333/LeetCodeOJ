public class Solution {
    public int[] singleNumber(int[] nums) {
        int[] ans = new int[2];
        if(nums.length <=2) 
            return nums;
        int result = 0;
        for(int i = 0; i < nums.length;++i) {
            result = result ^ nums[i];
        }
        
        int x = 1;
        while((x & result) ==0) {
            x = x << 1;
        }
        
        for(int i = 0; i < nums.length; ++i) {
            if((nums[i] & x) == x) {
                ans[0] = ans[0] ^ nums[i];
            } else {
                ans[1] = ans[1] ^ nums[i];
            }
        }
        
        return ans;
    }
}