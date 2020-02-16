class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def getLives(x,y,board):
            count = 0
            dx = [-1,0,1,-1,1,-1,0,1]
            dy = [1,1,1,0,0,-1,-1,-1]
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx<0 or ny<0 or nx>= len(board) or ny >= len(board[0]):
                    count += 0
                else:
                    count += board[nx][ny] & 1
            return count
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                lives = getLives(x,y,board)
                if lives == 3 or board[x][y] + lives == 3:
                    board[x][y] |= 2
        for x in range(len(board)):
            for y in range(len(board[0])):
                board[x][y] >>= 1
                