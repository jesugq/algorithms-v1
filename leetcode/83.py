class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        root = head
        node = root

        while node is not None:
            node = self.findNextUnique(node)
            node = node.next

        return root

    def findNextUnique(self, node: ListNode) -> ListNode:
        parent = node
        node = node.next

        while node is not None:
            if node.val != parent.val:
                break
            node = node.next
        
        parent.next = node
        return parent

class Main:
    def execute(self):
        solution = Solution()
        head = self.one()
        answer = solution.deleteDuplicates(head)
        
        head = answer
        while head is not None:
            print(head.val)
            head = head.next

    def one(self):
        c = ListNode(2)
        b = ListNode(1, c)
        a = ListNode(1, b)
        return a
    
    def two(self):
        e = ListNode(3)
        d = ListNode(3, e)
        c = ListNode(2, d)
        b = ListNode(1, c)
        a = ListNode(1, b)
        return a
    
main = Main()
main.execute()            