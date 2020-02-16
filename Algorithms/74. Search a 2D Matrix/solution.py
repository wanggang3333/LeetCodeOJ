class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        low = 0; high = m - 1
        while low <= high:
            mid = (low + high) / 2
            if matrix[mid][0] < target:
                low = mid + 1
            elif matrix[mid][0] > target:
                high = mid - 1
            else:
                return True
        m = high
        print m
        low = 0; high = n - 1
        while low <= high:
            mid = (low + high) / 2
            print "m,mid:",matrix[m][mid]
            if matrix[m][mid] < target:
                low = mid + 1
            elif matrix[m][mid] > target:
                high = mid - 1
            else:
                return True
        return False
        
                
        