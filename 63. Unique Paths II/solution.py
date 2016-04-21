class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        item = [1] * m
        array = [item] * n
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    array[i][j] = 0
                elif i != 0 and j != 0:
                    array[i][j] = array[i-1][j] + array[i][j-1]
                elif i == 0 and j == 0:
                    array[i][j] = 1
                elif i == 0 and j != 0:
                    array[i][j] = array[i][j-1]
                else:
                    array[i][j] = array[i-1][j]
        return array[n-1][m-1]