# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        t = head; h = head

        while(t != None and h != None):
            t = t.next
            if h.next != None:
                h = h.next.next
            else:
                h = None
            if (t != None and h != None and t == h):
                return True

        return False