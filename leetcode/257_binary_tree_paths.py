from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self, paths=list()):
        self.paths = paths

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.paths = list()
        path = ''
        self.generatePaths(root, path)
        return self.paths

    def generatePaths(self, node: TreeNode, path: str):
        if (node == None):
            return
        
        path += self.generateStep(node.val, path)

        if (self.isLeaf(node)):
            self.generatePath(path)
        else:
            self.generatePaths(node.left, path)
            self.generatePaths(node.right, path)

    def isLeaf(self, node: TreeNode) -> bool:
        return node.left == None and node.right == None

    def generateStep(self, val: int, path: str) -> str:
        if len(path) == 0:
            return str(val)
        else:
            return '->' + str(val)

    def generatePath(self, path: str) -> str:
        self.paths.append(path)

five = TreeNode(5)
two = TreeNode(2, None, five)
three = TreeNode(3)
one = TreeNode(1, two, three)

none = None

solution = Solution()
answer = solution.binaryTreePaths(one)
print(answer)