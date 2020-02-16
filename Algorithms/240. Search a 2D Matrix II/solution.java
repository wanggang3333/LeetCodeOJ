class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix[0])
        m = len(matrix)
        for i in range(m):
            y = self.binSearch(matrix[i],target)
            if matrix[i][y] == target:
                return True
        return False
        
        
    def binSearch(self,nums, target):
        n = len(nums)
        left = 0
        right = n-1
        while left <= right:
            mid = left + (right -left)/2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left + (right -left)/2