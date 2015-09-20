public class Solution {
    public void moveZeroes(int[] nums) {
        int p = nums.length;
        for(int i=0; i < p; ++i) {
            if(nums[i] == 0) {
                for(int j = i; j < p-1; ++j) {
                    nums[j] = nums[j+1];
                }
                nums[p-1] = 0;
                p = p-1;
                --i;
            }
        }
    }
}