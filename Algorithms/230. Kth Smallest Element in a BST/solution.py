#coding:utf-8
#先中序遍历BST生成一个列表，然后取第k个元素即可。


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        queue = self.inorderTraversal(root)
        return queue[k-1].val
        
    #中序遍历采用递归实现    
    def inorderTraversal(self, root):
        queue = []
        if root == None:
            return queue
        leftQueue = self.inorderTraversal(root.left)
        queue.extend(leftQueue)
        queue.append(root)
        rightQueue = self.inorderTraversal(root.right)
        queue.extend(rightQueue)
        return queue