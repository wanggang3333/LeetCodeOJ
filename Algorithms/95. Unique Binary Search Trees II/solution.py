# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.dfs(1,n)
            
    def dfs(self, start, end):
        if start > end:
            return [None]
        result = []
        for i in range(start,end+1):
            leftArray = self.dfs(start,i-1)
            rightArray = self.dfs(i+1,end)
            for m in leftArray:
                for n in rightArray:
                    root = TreeNode(i)
                    root.left = m
                    root.right = n
                    result.append(root)
        return result
        