public class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if(nums == null && nums.length == 0) 
            return res;
		//Arrays.sort()对基本数据类型采用的是“经过优化”的快速排序算法，升序排列
        Arrays.sort(nums);
        for(int i =0; i < nums.length; ++i) {
            List<Integer> sub = new ArrayList<Integer>();
            if(i>0 && nums[i] == nums[i-1]){
                continue;
            }
            int sum = - nums[i];
            int p = i+1, q = nums.length - 1;
            while(p < q) {
                if(sum == nums[p] + nums[q]) {
                    sub.add(nums[i]);
                    sub.add(nums[p]);
                    sub.add(nums[q]);
                    res.add(sub);
                    sub = new ArrayList<Integer>();
                    while(p+1<q && nums[p+1]==nums[p]) {
                        p++;
                    }
                    p++;
                    while(q-1>p && nums[q]==nums[q-1]) {
                        q--;
                    }
                    q--;
                } else if(nums[q]+nums[p]>sum) {
                    q--;
                } else {
                    p++;
                }
            }
        }
        return res;
    }
}