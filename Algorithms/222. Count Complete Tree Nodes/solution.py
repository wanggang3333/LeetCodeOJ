# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        lh = 0
        rh = 0
        leftTree = rightTree = root
        while leftTree:
            lh += 1
            leftTree =leftTree.left
        while rightTree:
            rh += 1
            rightTree = rightTree.right
        print lh
        if lh == rh:
            return (1<<lh) - 1
        return self.countNodes(root.left)+self.countNodes(root.right)+1