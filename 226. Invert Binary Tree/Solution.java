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
    public TreeNode invertTree(TreeNode root) {
        if(root == null) {
            return root;
        }
        TreeNode left,right;
        if(root.left != null) {
            right = invertTree(root.left);
        } else {
            right = null;
        }
        if(root.right != null) {
            left = invertTree(root.right);
        } else {
            left = null;
        }
        root.left = left;
        root.right = right;
        return root;
        
    }
}