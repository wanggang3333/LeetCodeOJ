# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0 or head == None:
            return head
        count = 0
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while p.next:
            p = p.next
            count += 1
        p.next = dummy.next
        step = count - (k%count)
        for i in range(step):
            p = p.next
        head = p.next
        p.next = None
        return head
            
        
        