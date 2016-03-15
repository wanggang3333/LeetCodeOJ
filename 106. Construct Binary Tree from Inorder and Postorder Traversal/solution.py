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
        n = len(inorder)
        if n == 0:
            return None
        if n == 1:
            return TreeNode(inorder[0])
        root = TreeNode(postorder[-1])
        index = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[0:index],postorder[0:index])
        root.right = self.buildTree(inorder[index+1:n],postorder[index:n-1])
        return root
        