# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        lens = 0
        temp = root
        while(temp):
            lens += 1
            temp = temp.next
        average = lens // k
        largerCnt = lens % k
        ans = []
        for i in range(k):
            ans.append(root)
            if root:
                if i < largerCnt:
                    for j in range(average):
                        root = root.next
                    temp = root.next
                    root.next = None
                    root = temp
                else:
                    for j in range(average-1):
                        root = root.next
                    temp = root.next
                    root.next = None
                    root = temp
        return ans
        