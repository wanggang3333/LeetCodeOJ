# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.preorder, self.inorder = preorder, inorder
        n = len(inorder)
        return self.dfs(0,0,n)
        
    def dfs(self, prestart,instart,n):
        if n == 0:
            return None
        root = TreeNode(self.preorder[prestart])
        index = self.inorder.index(self.preorder[prestart])
        leftLen = index - instart
        right = n -1- (index - instart)
        root.left = self.dfs(prestart+1,instart,index-instart)
        root.right = self.dfs(prestart+index-instart+1,index+1,n-1-(index-instart))
        return root