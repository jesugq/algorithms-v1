class Main {
    public static void main(String[] args) {
        TreeNode fifteen = new TreeNode(15);
        TreeNode seven = new TreeNode(7);
        TreeNode twenty = new TreeNode(20, fifteen, seven);

        TreeNode nine = new TreeNode(9);

        TreeNode three = new TreeNode(3, nine, twenty);

        TreeNode broken = null;

        Solution solution = new Solution();
        System.out.println(solution.maxDepth(three));
    }
}