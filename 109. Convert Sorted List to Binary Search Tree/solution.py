# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head == None:
            return None
        len = 0
        p = head
        while p:
            len += 1
            p = p.next
        array = []
        p = head
        while p:
            array.append(p.val)
            p = p.next
        return self.generate(array,0,len-1)
    
    def generate(self, array, start, end):
        if start > end:
            return None
        mid = start + (end - start)/2
        root = TreeNode(array[mid])
        root.left = self.generate(array,start,mid-1)
        root.right = self.generate(array,mid+1, end)
        return root