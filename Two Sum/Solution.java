public class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
        for(int i = 0;i < nums.length; ++i) {
            map.put(nums[i],i);
        }
        int[] index = new int[]{0,0};
        for(int i = 0; i < nums.length; ++i) {
            int find = target - nums[i];
            if(map.get(find) != null && map.get(find) != i) {
                index[0] = i +1;
                index[1] = map.get(find) + 1;
                break;
            }
        }
        return index;
    }
}