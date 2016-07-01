class Solution {
public:
    int singleNumber(vector<int>& nums) {
		//求异或，相同数的异或为0,而 0^a = a
        int sum = 0;//异或结果
        int len = nums.size();
        for(int i = 0 ; i < len; ++i){
            sum = sum ^ nums[i];
        }
        
        return sum;
    }
};