public class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> sum = new ArrayList<String>();
        
        if(nums.length == 0)
            return sum;
            
        int i = nums[0];
        int j = i - 1;
        String str = new String();
        
        for(int k = 1; k < nums.length; ++k) {
            if(nums[k] == nums[k-1] + 1)
                j = nums[k];
            else {
                if(j == i - 1) {
                    str ="" + i;
                     sum.add(str);
                } else {
                    str = i + "->" + j;
                    sum.add(str);
                }
                str = new String();
                i = nums[k];
                j = i - 1;
            }
                
        }
        if(j == i - 1) {
            str ="" + i;
            sum.add(str);
        } else {
            str = i + "->" + j;
            sum.add(str);
        }
        
        return sum;
            
    }
}