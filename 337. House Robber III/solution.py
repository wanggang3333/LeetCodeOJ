# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.difrob(root)[0]
        
    def difrob(self, root):
        if not root: return 0,0
        rob_left, no_rob_left = self.difrob(root.left)
        rob_right, no_rob_right = self.difrob(root.right)
        return max(rob_left+rob_right, no_rob_left+no_rob_right+root.val),rob_left + rob_right
        