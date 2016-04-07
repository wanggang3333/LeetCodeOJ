# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        pre = dummy
        sign = 0
        while l1 or l2 or sign:
            if l1 and l2:
                num = l1.val + l2.val + sign
                l1 = l1.next; l2 = l2.next
            elif l1:
                num = l1.val + sign
                l1 = l1.next
            elif l2:
                num = l2.val + sign
                l2 = l2.next
            else:
                num = sign
                
            if num>=10:
                newlist = ListNode(num%10)
                sign = 1
            else:
                newlist = ListNode(num)
                sign = 0
            pre.next = newlist
            pre = newlist
        return dummy.next
            