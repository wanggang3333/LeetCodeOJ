class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None:
            return 0
        n = len(nums)
        take = 0
        notake = 0
        profit = 0
        i = 0
        while i < n:
            take = notake + nums[i]
            notake = profit
            profit = max(take, notake)
            i += 1
        return profit
        