# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    count = 0
    queue = []
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.queue = self.preorderTraversal(root)
        self.length = len(self.queue)
        self.count = 0
        
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.count < self.length
        

    def next(self):
        """
        :rtype: int
        """
        result = self.queue[self.count].val
        self.count += 1
        return result
        
    def preorderTraversal(self, root):
        queue = []
        if root == None:
            return queue
        queue.extend(self.preorderTraversal(root.left))
        queue.append(root)
        queue.extend(self.preorderTraversal(root.right))
        return queue

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())