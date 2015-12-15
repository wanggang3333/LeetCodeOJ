class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #return min(nums)
        first = 0; last = len(nums) -1
        ans = nums[0]
        while first <= last:
            mid =(last + first)/2
            if nums[mid] <= nums[last]:
                last = mid - 1
            else:
                first = mid + 1
            if nums[mid] < ans:
                ans = nums[mid]
        return ans