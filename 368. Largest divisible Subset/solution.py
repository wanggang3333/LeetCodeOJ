class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        n = len(nums)
        dp = [0] * n
        idx = [-1] * n
        max_dp = 0
        max_inx = 0
        nums.sort()
        for i in xrange(n):
            for j in xrange(i):
                if nums[i] % nums[j] == 0 and dp[j]+1 > dp[i]:
                    dp[i] = dp[j] + 1
                    idx[i] = j
            if dp[i] > max_dp:
                max_dp = dp[i]
                max_inx = i
        ans = []
        while max_inx != -1:
            ans.append(nums[max_inx])
            max_inx = idx[max_inx]
        return ans
        