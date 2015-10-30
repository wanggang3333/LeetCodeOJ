/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int len1 = 0, len2 = 0;
        ListNode p1 = headA;
        ListNode p2 = headB;
        if(p1 == null || p2 == null)
            return null;
        while(p1 != null) {
            len1++;
            p1 = p1.next;
        }
        while(p2 != null) {
            len2++;
            p2 = p2.next;
        }
        int diff = 0;
        p1 = headA;
        p2 = headB;
        
        if(len1 > len2) {
            diff = len1 - len2;
            while(diff != 0) {
                p1 = p1.next;
                diff--;
            }
        }
        if(len2 > len1) {
            diff = len2 - len1;
            while(diff != 0) {
                p2 = p2.next;
                diff--;
            }
        }
        while(p1 != null && p2 != null) {
            if(p1.val == p2.val && p1.next == p2.next) {
                return p1;
            }
            p1 = p1.next;
            p2 = p2.next;
        }
        return null;
            
    }
}