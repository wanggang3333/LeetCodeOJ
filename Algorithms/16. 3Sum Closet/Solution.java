public class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int minDis = Integer.MAX_VALUE;
        int value = 0;
        Arrays.sort(nums);
        for(int i=0; i < nums.length; ++i) {
            if(i > 0 && nums[i]==nums[i-1]) {
                continue;
            }
            int p = i+1, q = nums.length - 1;
            while(p < q) {
                int distance = nums[i] + nums[p] + nums[q] - target;
                if(distance == 0) {
                    return target;
                } else if(distance < 0) {
                    if(minDis >= (-distance)) {
                        minDis = -distance;
                        value = nums[i] + nums[p] + nums[q];
                    }
                    p++;
                } else {
                    if(minDis >= distance) {
                        minDis = distance;
                        value = nums[i] + nums[p] + nums[q];
                    }
                    q--;
                }
            }
        }
        return value;
    }
}