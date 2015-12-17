# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res =[]; stack = []
        if root ==None:
            return res
        while root or stack:
            if root:
                stack.append(root)
                res.append(root.val)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        return res

        