import sys
import bisect

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.node_values: List[int] = []
        self.length: int = 0

    def minDiffInBST(self, root: TreeNode) -> int:
        self.discover_node_values(root)
        return self.get_smallest_difference()

    def discover_node_values(self, node: TreeNode) -> None:
        if not node:
            return
        bisect.insort(self.node_values, node.val)
        self.length += 1
        self.discover_node_values(node.left)
        self.discover_node_values(node.right)

    def get_smallest_difference(self) -> int:
        smallest_difference: int = sys.maxsize
        for i in range(1, self.length):
            previous_value = self.node_values[i-1]
            current_value = self.node_values[i]
            difference = current_value - previous_value
            if difference < smallest_difference:
                smallest_difference = difference
        return smallest_difference

class Main:
    def execute(self):
        self.test_1()
        self.test_2()
        self.test_3()

    def test_1(self):
        solution = Solution()
        one = TreeNode(1)
        three = TreeNode(3)
        two = TreeNode(2, one, three)
        six = TreeNode(6)
        four = TreeNode(4, two, six)
        print(solution.minDiffInBST(four))

    def test_2(self):
        solution = Solution()
        twelve = TreeNode(12)
        fortynine = TreeNode(49)
        zero = TreeNode(0)
        fortyeight = TreeNode(48, twelve, fortynine)
        one = TreeNode(1, zero, fortyeight)
        print(solution.minDiffInBST(one))

    def test_3(self):
        solution = Solution()
        fiftytwo = TreeNode(52)
        fortynine = TreeNode(49, None, fiftytwo)
        eightynine = TreeNode(89)
        sixtynine = TreeNode(69, fortynine, eightynine)
        ninety = TreeNode(90, sixtynine, None)
        print(solution.minDiffInBST(ninety))

main = Main()
main.execute()