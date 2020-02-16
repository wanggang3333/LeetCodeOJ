class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        res = []
        item = [sum(grid[0][:i+1]) for i in range(n)]
        res.append(item)
        for i in range(1,m):
            item = []
            for j in range(n):
                if j == 0:
                    ans = res[i-1][0] + grid[i][j]
                else:
                    ans = min(res[i-1][j],item[j-1]) + grid[i][j]
                item.append(ans)
            res.append(item)
        return res[m-1][n-1]