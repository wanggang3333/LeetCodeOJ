class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': continue
                tmp = board[i][j]
                board[i][j] = 'D'
                if self.isValid(i,j,tmp,board):
                    board[i][j] = tmp
                else:
                    return False
        return True
        
        
    def isValid(self, x, y, val, board):
        for i in range(9):
            if board[x][i] == val:
                return False
        for j in range(9):
            if board[j][y] == val:
                return False
        for i in range(3):
            for j in range(3):
                if board[(x/3)*3+i][(y/3)*3+j] == val:
                    return False
        return True
        
        