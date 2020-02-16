# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        print head.val
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        p1,p2 = head, slow.next
        slow.next = None
        p1 = self.sortList(p1)
        p2 = self.sortList(p2)
        return self.merge(p1,p2)
    
    def merge(self, p1, p2):
        if p1 == None:
            return p2
        if p2 == None:
            return p1
        dummy = ListNode(0)
        p = dummy
        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
                p = p.next
            else:
                p.next = p2
                p2 = p2.next
                p = p.next
        if p1 == None:
            p.next = p2
        if p2 == None:
            p.next = p1
        return dummy.next

        