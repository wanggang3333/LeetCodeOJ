class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = n-1
        while left <= right:
            mid = (left + right) / 2
            if (mid == 0 or nums[mid] >= nums[mid -1]) and (mid == n-1 or nums[mid] >= nums[mid + 1]):
                return mid
            elif mid > 0 and nums[mid - 1] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return mid