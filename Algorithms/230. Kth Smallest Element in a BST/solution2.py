#coding:utf-8
#中序遍历到第k个值
#中序遍历采用迭代实现

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
        if root == None:
            return None
        node = root
        stack = []
        while node:
            stack.append(node)
            node = node.left
        x = 1
        while stack and x <=k:
            node = stack.pop()
            x += 1
            rightnode = node.right
            while rightnode:
                stack.append(rightnode)
                rightnode = rightnode.left
        return node.val
        