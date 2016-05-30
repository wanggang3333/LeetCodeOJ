class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        idx , ans, known = 0, 0, 1
        size = len(nums)
        while known <= n:
            if idx < size and nums[idx] <= known:
                known += nums[idx]
                idx += 1
            else:
                known <<= 1
                ans += 1
        return ans
        