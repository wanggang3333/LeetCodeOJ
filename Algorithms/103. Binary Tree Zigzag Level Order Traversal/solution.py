# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root == None:
            return res
        queue = []
        queue.append(root)
        isLeft = True
        while queue:
            new_queue = []
            nodelist = [n.val for n in queue]
            if isLeft:
                res.append(nodelist)
            else:
                nodelist.reverse()
                res.append(nodelist)
            for n in queue:
                if n.left:
                    new_queue.append(n.left)
                if n.right:
                    new_queue.append(n.right)
            isLeft = not isLeft
            queue = new_queue
        return res
        