class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == []:
            return 0
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    self.searchIslands(grid,i,j)
        return res
                    
        
        
        
    def searchIslands(self, grid, i, j):
        grid[i][j] = "0"
        if i>0 and grid[i-1][j] == "1": self.searchIslands(grid,i-1,j)
        if j>0 and grid[i][j-1] == "1": self.searchIslands(grid,i,j-1)
        if i < len(grid)-1 and grid[i+1][j] == "1": self.searchIslands(grid, i+1,j)
        if j < len(grid[0])-1 and grid[i][j+1] == "1": self.searchIslands(grid, i, j+1)
        