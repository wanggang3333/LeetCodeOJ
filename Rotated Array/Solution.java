public class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        int[] nums2 = new int[n];
        for(int i = 0; i < n-1; ++i) {
            nums2[i] = nums[(i - k + n) % n];
        }
        for(int i = 0; i < n-1; ++i) {
            nums[i] = nums2[i];
        }
    }
}