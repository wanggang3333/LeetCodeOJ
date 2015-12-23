# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums or len(nums) == 0:
            return None
        root = TreeNode(0)
        lengths = len(nums)
        if lengths == 1:
            root.val = nums[0]
            root.left = None
            root.right = None
        elif lengths == 2:
            root.val = nums[1]
            root.left = TreeNode(nums[0])
            root.right = None
        else:
            mid = len(nums)/2
            root.val = nums[mid]
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid+1:])
        return root