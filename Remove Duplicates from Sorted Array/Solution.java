public class Solution {
	//时间复杂度O（n）,空间复杂度O(1)
    public int removeDuplicates(int[] nums) {
        int lens = nums.length;
        if(lens == 0)
            return 0;
        int count = 0;
        for(int i = 1; i < nums.length; ++i) {
            if(nums[count] != nums[i]) {
                nums[++count] = nums[i];
            }
        }
        
        return count+1;
    }
}