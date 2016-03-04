# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        else :
            return self.childIsSymmetrics(root.left, root.right)
    
    def childIsSymmetrics(self, p, q):
        if p == None and q == None:
            return True
        elif p and q and p.val == q.val:
            return self.childIsSymmetrics(p.left, q.right) and self.childIsSymmetrics(p.right, q.left)
        else :
            return False
        