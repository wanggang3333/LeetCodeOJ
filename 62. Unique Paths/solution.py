class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        item = [1] * m
        array = [item] * n
        for i in range(1,n):
            for j in range(1,m):
                array[i][j] = array[i-1][j] + array[i][j-1]
        return array[n-1][m-1]