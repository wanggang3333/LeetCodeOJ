public class Solution {
    public void rotate(int[] nums, int k) {
        k = k % nums.length;
        rev(nums, 0, nums.length-1);
        rev(nums, 0 , k-1);
        rev(nums, k, nums.length -1);
    }
    private void rev(int[] nums, int left, int right) {
        while(left < right) {
            int temp = nums[right];
            nums[right--] = nums[left];
            nums[left++] = temp;
        }
    }
}