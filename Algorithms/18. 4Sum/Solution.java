public class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if(nums == null || nums.length <3)
            return res;
        for(int i = 0;i < nums.length; ++i) {
            if(i > 0 && nums[i]==nums[i-1])
                continue;
            for(int j = i+1; j < nums.length - 2; ++j) {
                if(j > i+1 && nums[j] == nums[j-1]) {
                    continue;
                }
                int p = j+1, q = nums.length - 1;
                List<Integer> sub = new ArrayList<Integer>();
                while(p < q) {
                    int sum = nums[i] + nums[j] + nums[p] + nums[q];
                    if(target == sum) {
                        sub.add(nums[i]);
                        sub.add(nums[j]);
                        sub.add(nums[p]);
                        sub.add(nums[q]);
                        res.add(sub);
                        sub = new ArrayList<Integer>();
                        while(p < q && nums[p] == nums[p+1]) {
                            p++;
                        }
                        p++;
                        while(q >p && nums[q] == nums[q-1]) {
                            q--;
                        }
                        q--;
                    } else if(sum > target) {
                        q--;
                    } else {
                        p++;
                    }
                }
            }
        }
        return res;
    }
}