class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [1]*n
        
        for i in range(n-2,-1,-1):
            result[i] = result[i+1] * nums[i+1]
            
        left = 1
        for i in range(n):
            result[i] = result[i] * left
            left = left * nums[i]
            
        return result
            