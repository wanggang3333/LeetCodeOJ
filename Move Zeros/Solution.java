public class Solution {
	/*在i和p之间循址数组(i,p)
	*如果i处数值为0，数组（i,p）左移，然后p-1处置为零,p--,来缩小循址区间；
	*如果i处数值不为0，i++，循址下一处，缩小循址空间。
	*此方法涉及较多的数组操作
	*如：[0,0,.....,0,0,1],则需要的数组赋值操作为 (n-1)*(n-2)*...*2*1
	*/
    public void moveZeroes(int[] nums) {
        int p = nums.length;
        for(int i=0; i < p; ++i) {
            if(nums[i] == 0) {
                for(int j = i; j < p-1; ++j) {
                    nums[j] = nums[j+1];
                }
                nums[p-1] = 0;
                p = p-1;
                --i;
            }
        }
    }
}