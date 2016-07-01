# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        pPath = self.findPath(root,p); qPath = self.findPath(root,q)
        res = None; x = 0
        length = min(len(pPath), len(qPath))
        while x < length and pPath[x] == qPath[x]:
            res = pPath[x]
            x = x + 1
        return res
    
    
    def findPath(self, root, target):
        stack = []
        lastPoint = None
        while stack or root:
            if root:
                stack.append(root)
                if root == target:
                    return stack
                root = root.left

            else:
                peek = stack[-1]
                if peek.right and lastPoint != peek.right:
                    root = peek.right
                else:
                    lastPoint = stack.pop()
                    root = None
        return Stack
        