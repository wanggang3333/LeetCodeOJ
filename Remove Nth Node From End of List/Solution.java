/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if(head == null)
            return head;
        ListNode p = head;
        int lens = 0;
        while(p != null) {
            lens++;
            p = p.next;
        }
        int fromStart = lens - n + 1;
        
        if(fromStart == 1)
            return head.next;
        p = head;
        int i = 0;
        while(p != null) {
            i++;
            if(i == fromStart - 1)
                p.next = p.next.next;
            p = p.next;
        }
        return head;
    }
}