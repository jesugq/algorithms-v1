class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    ZERO = 0
    BASE_TWO = 2

    def sumRootToLeaf(self, root: TreeNode) -> int:
        binary = '0'
        return self.sumRootToLeafBinary(root, binary)

    def sumRootToLeafBinary(self, node: TreeNode, binary: str) -> int:
        if self.nodeIsNull(node):
            return self.ZERO        
        binary += self.stringOfInteger(node.val)
        if self.nodeIsLeaf(node):
            return self.integerOfString(binary)

        return self.sumChildrenBinary(node, binary);

    def nodeIsNull(self, node: TreeNode) -> bool:
        return node == None

    def nodeIsLeaf(self, node: TreeNode) -> bool:
        return self.nodeIsNull(node.left) and self.nodeIsNull(node.right)
    
    def integerOfString(self, binary: str) -> int:
        return int(binary, self.BASE_TWO)

    def stringOfInteger(self, value: int) -> str:
        return str(value)

    def sumChildrenBinary(self, node: TreeNode, binary: str) -> int:
        return self.sumRootToLeafBinary(node.left, binary) + self.sumRootToLeafBinary(node.right, binary)