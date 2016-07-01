/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;2
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode reverseList(ListNode head) {
        if(head == null || head.next == null)
            return head;
        
        ListNode now = head;
        ListNode nex = head.next;
        head.next = null;
        while(now != null && nex != null) {
            ListNode nexnex = nex.next;
            nex.next = now;
            now = nex;
            if(nexnex != null)
                nex = nexnex;
            else
                break;
        }
        return nex;
    }
}