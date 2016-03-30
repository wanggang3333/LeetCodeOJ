# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if fast and slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return fast
        return None