class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == []:
            return 0
        m,n = len(matrix), len(matrix[0])
        dp = [[0]*n for i in range(m)]
        ans = 0
        for i in range(n):
            dp[0][i] = int(matrix[0][i])
            ans = max(ans, dp[0][i])
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            ans = max(ans, dp[i][0])
        for x in range(1,m):
            for y in range(1,n):
                if int(matrix[x][y]):
                    dp[x][y] = min(dp[x-1][y-1],dp[x-1][y],dp[x][y-1])+1
                    ans = max(ans, dp[x][y])
        return ans * ans