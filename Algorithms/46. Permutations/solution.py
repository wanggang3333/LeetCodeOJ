class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0: return [[]]
        if len(nums) == 1: return [[nums[0]]]
        res = []
        for i in range(len(nums)):
            newList = self.permute(nums[:i] + nums[i+1:])
            for j in newList:
                res.append([nums[i]]+j)
        return res