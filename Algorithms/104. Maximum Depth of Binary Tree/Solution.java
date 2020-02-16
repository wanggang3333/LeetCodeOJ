/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public int maxDepth(TreeNode root) {
        if(root == null) {
            return 0;
        }
        int level = 0;
        LinkedList<TreeNode> queue = new LinkedList<TreeNode>();
        queue.add(root);
        int curNum = 1;
        int nextNum = 0;
        while(!queue.isEmpty()) {
            TreeNode n = queue.poll();
            curNum--;
            if(n.left != null) {
                queue.add(n.left);
                nextNum++;
            }
            if(n.right != null) {
                queue.add(n.right);
                nextNum++;
            }
            if(curNum == 0) {
                curNum = nextNum;
                nextNum = 0;
                level++;
            }
        }
        return level;
    }
}