public class Solution {
	/*i,jΪ�����±꣬i����ָʾ�洢λ�ñ仯��j����ѭַ�����ֵ��
	*����j����ֵΪ0���������������ж���һ����ֵ��
	*����j������ֵ��Ϊ0ʱ����j����ֵ�洢��i���������ж���һ����ֵ��
	*��i==jʱ��˵��ָ��ͬһ��������ʱ��ֵ��Ϊ��ʱ��i��jͬʱ��һ�����Լ�������Ĳ�����
	*����i���ֵ����Ϊ�㡣
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