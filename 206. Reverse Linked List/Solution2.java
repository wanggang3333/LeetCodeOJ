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
        
        ListNode second = head.next;
        ListNode ans = reverseList(second);
        second.next = head;
        head.next = null;
        return ans;
    }
}