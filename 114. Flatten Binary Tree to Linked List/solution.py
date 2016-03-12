# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root == None:
            return
        result = []
        result = self.inorderTraversal(root)
        root = head = result[0]
        n = len(result)
        for i in range(1,n):
            head.left = None
            head.right = result[i]
            head = result[i]
        
        
        
    def inorderTraversal(self, root):
        result = []
        if root == None:
            return result
        result.append(root)
        result.extend(self.inorderTraversal(root.left))
        result.extend(self.inorderTraversal(root.right))
        return result
        