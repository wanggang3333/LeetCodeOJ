class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import random
        more =[]; less = []
        pivot = random.choice(nums)
        for num in nums:
            if num > pivot:
                more.append(num)
            if num < pivot:
                less.append(num)
        if k <= len(more):
            return self.findKthLargest(more,k)
        elif k > len(nums) - len(less):
            return self.findKthLargest(less,k-(len(nums)-len(less)))
        else:
            return pivot