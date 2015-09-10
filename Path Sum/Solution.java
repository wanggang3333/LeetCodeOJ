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
    public boolean hasPathSum(TreeNode root, int sum) {
        if(root == null){
            return false;
        }
        int nextSum = sum - root.val;
        TreeNode leftChild = root.left;
        TreeNode rightChild = root.right;
        if(leftChild != null && rightChild != null){
            return(hasPathSum(leftChild,nextSum) || hasPathSum(rightChild,nextSum));
        }else if(leftChild != null && rightChild == null){
            return(hasPathSum(leftChild,nextSum));
        }else if(leftChild == null && rightChild != null){
            return(hasPathSum(rightChild,nextSum));
        }else{
            return (root.val == sum);
        }
    }
}