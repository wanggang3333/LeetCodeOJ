# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = []
        result = []
        if root == None:
            return result
        queue.append(root)
        while queue:
            new_queue = []
            result.append([n.val for n in queue])
            for n in queue:
                if n.left:
                    new_queue.append(n.left)
                if n.right:
                    new_queue.append(n.right)
            queue = new_queue
        result.reverse()
        return result