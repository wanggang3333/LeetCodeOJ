class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        return max(self.roblinear(nums[:-1]), self.roblinear(nums[1:]))
        
        
    def roblinear(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p2 = 0
        p1 = 0
        for i in range(len(nums)):
            maxs = max(p2+nums[i],p1)
            p2 = p1
            p1 = maxs
        return p1