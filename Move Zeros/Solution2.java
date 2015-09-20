public class Solution {
	/*i,j为数组下标，i用于指示存储位置变化，j用于循址数组的值。
	*数组j处数值为0，不做处理，继续判断下一处的值；
	*数组j处的数值不为0时，把j处的值存储到i处，继续判断下一处的值；
	*当i==j时，说明指向同一处，当此时数值不为零时，i和j同时加一，可以减少数组的操作。
	*最后把i后的值都置为零。
	*/
	
    public void moveZeroes(int[] nums) {
        int i=0, j=0;
        while(j < nums.length) {
            if(nums[j] == 0) {
            }else if(i == j) {
                i++;
            }else {
                nums[i] = nums[j];
                i++;
            }
			j++;
        }
        while(i < nums.length) {
            nums[i] = 0;
            i++;
        }
    }
}