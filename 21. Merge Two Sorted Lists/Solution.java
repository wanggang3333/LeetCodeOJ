/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if(l1 == null)
            return l2;
        if(l2 == null)
            return l1;
            
        ListNode p1 = l1;
        ListNode p2 = l2;
        ListNode hd;
        ListNode list;
        if(l1.val <= l2.val) {
            hd = l1;
            list = l1;
            p1 = l1.next;
        } else {
            hd = l2;
            list = l2;
            p2 = l2.next;
        }
        
        while(p1 != null && p2 != null) {
            if(p1.val <= p2.val) {
                list.next = p1;
                list = p1;
                p1 = p1.next;
            } else {
                list.next = p2;
                list = p2;
                p2 = p2.next;
            }
        }
        
        if(p1 == null) {
            list.next = p2;
        } else {
            list.next = p1;
        }
        
        return hd;
    }
}