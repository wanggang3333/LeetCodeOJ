# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        p = head
        smaller = dummy1
        bigger = dummy2
        while p:
            if p.val < x:
                smaller.next = p
                p = p.next
                smaller = smaller.next
            else:
                bigger.next = p
                p = p.next
                bigger = bigger.next
        smaller.next = dummy2.next
        bigger.next = None
        return dummy1.next
                