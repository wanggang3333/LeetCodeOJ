public class Solution {
    public int removeDuplicates(int[] nums) {
        if(nums.length < 3)
            return nums.length;
        int count = 0;
        int index = 0;
        for(int i = 1; i < nums.length; ++i) {
            if(nums[index] != nums[i]) {
                nums[++index] = nums[i];
                count = 1;
            } else if (count == 1) {
                nums[++index] = nums[i];
                count = 2;
            } 
        }
        
        return index + 1;
    }
}