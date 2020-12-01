/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
import java.lang.Math;

class Solution {
    class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public int maxDepth(TreeNode root) {
        int currentDepth = 1;
        return depthOfNode(root, currentDepth);
    }

    public int depthOfNode(TreeNode node, int currentDepth) {
        if (nodeIsNull(node)) {
            return currentDepth;
        }
        return deepestChildBetween(node.left, node.right, currentDepth + 1);
    }

    public boolean nodeIsNull(TreeNode node) {
        return node == null;
    }

    public int deepestChildBetween(TreeNode left, TreeNode right, int currentDepth) {
        return Math.max(depthOfNode(left, currentDepth), depthOfNode(right, currentDepth));
    }
}