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
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> ans = new ArrayList<String>();
        if (root == null) {
            return ans;
        }
        
        dfs(root,new StringBuilder(), ans);
        
        return ans;
    }
    
    public void dfs(TreeNode root, StringBuilder sb, List<String> ans) {
        if(root.left == null && root.right == null) {
            sb.append(root.val);
            ans.add(sb.toString());
            return;
        }
        
        sb.append(root.val);
        sb.append("->");
        if(root.left != null) {
            dfs(root.left, new StringBuilder(sb), ans);
        }
        if(root.right != null) {
            dfs(root.right, new StringBuilder(sb), ans);
        }
    }
}