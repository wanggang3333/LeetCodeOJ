class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1,-1]
        if nums == None or len(nums) == 0:
            return res
        ll = 0; lr = len(nums)-1
        while ll <= lr:
            mid = (ll + lr)/2
            if nums[mid] < target:
                ll = mid + 1
            else:
                lr = mid - 1
                
        rl = 0; rr = len(nums)-1
        while rl <= rr:
            mid = (rl + rr)/2
            if nums[mid] <= target:
                rl = mid + 1
            else:
                rr = mid - 1
        print ll, rr
        if ll > rr:
            return res
        res = [ll,rr]
        return res