public class Solution {
    public void nextPermutation(int[] nums) {
        if (nums == null && nums.length == 0 || nums.length == 1) {
            return;
        }

        //step 1: find the first small(partitionNumber)
        int i;
        for(i = nums.length-2; i >= 0; i--) {
            if(nums[i]<nums[i+1]){
                break;
            }
        }
        if(i < 0) {
            Arrays.sort(nums);
            return;
        }
        //step2: find changeNumber
        int j;
        for(j = nums.length -1; j > i; j--) {
            if(nums[j] > nums[i]) {
                break;
            }
        }
        //step3:swap the two numbers
        int temp = nums[j];
        nums[j] = nums[i];
        nums[i] = temp;
        Arrays.sort(nums,i+1,nums.length);
    }
}