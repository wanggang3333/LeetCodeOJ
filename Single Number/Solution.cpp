class Solution {
public:
    int singleNumber(vector<int>& nums) {
		//�������ͬ�������Ϊ0,�� 0^a = a
        int sum = 0;//�����
        int len = nums.size();
        for(int i = 0 ; i < len; ++i){
            sum = sum ^ nums[i];
        }
        
        return sum;
    }
};