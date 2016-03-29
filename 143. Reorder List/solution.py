# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None:
            return
        #split the list to two part
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        p1, p2 = head, slow.next;
        slow.next = None
        #reverse seconde part
        p2 = self.reverse(p2)
        #merge two part
        while p1 and p2:
            tmp1 = p1.next
            tmp2 = p2.next
            p1.next = p2
            p2.next = tmp1
            p1 = tmp1
            p2 = tmp2
        
        
    def reverse(self, head):
        if head == None or head.next == None:
            return head
        pre = None
        p = head
        while p:
            last = p.next
            p.next = pre
            pre = p
            p = last
        return pre
        
        
        
        
        