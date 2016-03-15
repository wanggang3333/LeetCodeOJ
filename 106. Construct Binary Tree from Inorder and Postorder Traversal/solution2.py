# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.inorder, self.postorder = inorder, postorder
        n = len(self.inorder)
        return self.dfs(0,0,n)
        
    def dfs(self,instart,postart,n):
        if n == 0:
            return None
        root = TreeNode(self.postorder[postart+n-1])
        index = self.inorder.index(self.postorder[postart+n-1])
        root.left = self.dfs(instart,postart,index - instart)
        root.right = self.dfs(index+1,postart+index-instart,n-1-(index-instart))
        return root
        
        