class Solution {
    public static final int ZERO = 0;

    public int sumOfLeftLeaves(TreeNode root) {
        return sumLeftLeaves(root, false);
    }

    public int sumLeftLeaves(TreeNode node, boolean nodeIsLeft) {
        if (nodeIsNull(node)) {
            return ZERO;
        }

        if (nodeIsLeft && nodeIsLeaf(node)) {
            return node.val;
        } else {
            return sumBothLeaves(node);
        }
    }

    public boolean nodeIsNull(TreeNode node) {
        return node == null;
    }

    public boolean nodeIsLeaf(TreeNode node) {
        return node.left == null && node.right == null;
    }

    public int sumBothLeaves(TreeNode node) {
        return sumLeftLeaves(node.left, true) + sumLeftLeaves(node.right, false);
    }
}