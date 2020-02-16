/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public void deleteNode(ListNode node) {
        if(node != null && node.next != null){
                ListNode nextNode = node.next;
                node.val = nextNode.val;
                node.next = nextNode.next;
        }
    }
}