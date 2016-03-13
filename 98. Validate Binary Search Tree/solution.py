# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if root == None:
            return True
        if  self.isValidBST(root.left) and self.isValidBST(root.right):
            leftMax = self.findMax(root.left)
            rightMin = self.findMin(root.right)
            if leftMax == None and rightMin == None:
                return True
            if leftMax == None and rightMin > root.val:
                return True
            if rightMin == None and leftMax < root.val:
                return True
            if leftMax < root.val and rightMin > root.val:
                return True
        return False
    
    def findMin(self, root):
        if root==None:
            return None
        while root.left:
            root = root.left
        return root.val
        
    def findMax(self, root):
        if root==None:
            return None
        while root.right:
            root = root.right
        return root.val
        