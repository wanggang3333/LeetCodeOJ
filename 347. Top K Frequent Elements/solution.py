class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counters = {}
        for num in nums:
            if num in counters:
                counters[num] += 1
            else:
                counters[num] = 1
        freList = []
        freList = [[] for i in range(len(nums) + 1)]
        for num in counters:
            freList[counters[num]].append(num)
        ans = []
        for i in freList[::-1]:
            ans += i
        return ans[:k]