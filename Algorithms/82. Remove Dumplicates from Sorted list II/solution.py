# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        dummy = ListNode(0)
        p1 = dummy
        p2 = head
        while p2:
            if not p2.next or p2.val != p2.next.val:
                p1.next = p2
                p2 = p2.next
                p1 = p1.next
            else:
                v = p2.val
                while p2 and p2.val == v:
                    p2 = p2.next
		p1.next = None # p1 is end of list
        return dummy.next