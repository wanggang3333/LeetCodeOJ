# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next or m == n:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = mcurr = ncurr = dummy
        # find the head of reverse list
        for i in range(m-1):
            mcurr = mcurr.next
        mhead = mcurr.next
        # find the end of reverse list 
        for i in range(n):
            ncurr = ncurr.next
        nend = ncurr.next
        ncurr.next = None
        #reverse and link
        mcurr.next = self.reverse(mhead)
        mhead.next = nend
        return dummy.next
        
        
    def reverse(self, head):
        if not head or not head.next:
            return head
        p = head
        pre = None
        while p:
            tmp = p.next
            p.next = pre
            pre = p
            p = tmp
        return pre
            
            
        