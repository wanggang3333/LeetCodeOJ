class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        numdict = dict()
        n = len(nums)
        for i in range(n):
            idx = numdict.get(nums[i])
            if idx >= 0 and i - idx <= k:
                return True
            else:
                numdict[nums[i]] = i
        return False
        