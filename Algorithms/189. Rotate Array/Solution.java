public class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        int[] nums2 = new int[n];
        for(int i = 0; i < n; ++i) {
			//Çë¼ûÇóÓà±Ê¼Ç
            int x = i -k +n;
            if(x < 0) {
                x = x + n;
            }
            x = x % n;
            nums2[i] = nums[x];
        }
        for(int i = 0; i < n; ++i) {
            nums[i] = nums2[i];
        }
    }
}