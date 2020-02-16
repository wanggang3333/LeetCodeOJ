# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root == None:
            return result
        queue = []
        queue.append(root)
        while queue:
            new_queue = []
            result.append(queue[-1].val)
            for n in queue:
                if n.left != None:
                    new_queue.append(n.left)
                if n.right != None:
                    new_queue.append(n.right)
            queue = new_queue
        return result
        
        