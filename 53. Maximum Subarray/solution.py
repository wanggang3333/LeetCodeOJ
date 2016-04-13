class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p1 = -2147483648; p2 = -2147483648
        for num in nums:
            p1 = max(p1+ num, num)
            p2 = max(p1,p2)
        return p2