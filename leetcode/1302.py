class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.tree_height = 0
        self.tree_sum = 0

    def deepestLeavesSum(self, root: TreeNode) -> int:
        root_height = 0
        self.make_tree_height(root, root_height)
        self.make_tree_sum(root, root_height)
        return self.tree_sum

    def node_is_none(self, node: TreeNode) -> bool:
        return node is None
    
    def node_is_leaf(self, node: TreeNode) -> bool:
        return node.left is None and node.right is None

    def make_tree_height(self, node: TreeNode, height: int) -> None:
        if self.node_is_none(node):
            return
        elif self.node_is_leaf(node):
            if height > self.tree_height:
                self.tree_height = height
        
        self.make_tree_height(node.left, height + 1)
        self.make_tree_height(node.right, height + 1)

    def make_tree_sum(self, node: TreeNode, height: int) -> None:
        if self.node_is_none(node):
            return
        elif self.node_is_leaf(node):
            if height == self.tree_height:
                self.tree_sum += node.val
        
        self.make_tree_sum(node.left, height + 1)
        self.make_tree_sum(node.right, height + 1)

class Main:
    def exec(self):
        solution = Solution()
        root = self.e1()
        answer = solution.deepestLeavesSum(root)
        print(answer)
    
    def e1(self):
        seven = TreeNode(7)
        eight = TreeNode(8)

        four = TreeNode(4, seven, None)
        five = TreeNode(5)
        six = TreeNode(6, None, eight)

        two = TreeNode(2, four, five)
        three = TreeNode(3, None, six)

        one = TreeNode(1, two, three)
        return one

main = Main()
main.exec()