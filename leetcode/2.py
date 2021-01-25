class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        la = ListNode()
        pointer_one = l1
        pointer_two = l2
        pointer_ans = la
        carry_ans = 0
        
        while pointer_ans is not None:
            value_one = pointer_one.val if pointer_one else 0
            value_two = pointer_two.val if pointer_two else 0

            summatory = value_one + value_two + carry_ans
            value_ans = int(summatory % 10)
            carry_ans = int(summatory / 10)

            pointer_ans.val = value_ans

            pointer_one = pointer_one.next if pointer_one else pointer_one
            pointer_two = pointer_two.next if pointer_two else pointer_two
            
            if pointer_one or pointer_two or carry_ans:
                pointer_ans.next = ListNode()
            pointer_ans = pointer_ans.next
            
        return la

class Main:
    def exec(self):
        solution = Solution()
        l1, l2 = self.e2()
        answer = solution.addTwoNumbers(l1, l2)
        while answer:
            print(answer.val)
            answer = answer.next

    def e1(self):
        l1_2 = ListNode(3)
        l1_1 = ListNode(4, l1_2)
        l1_0 = ListNode(2, l1_1)

        l2_2 = ListNode(4)
        l2_1 = ListNode(6, l2_2)
        l2_0 = ListNode(5, l2_1)

        return l1_0, l2_0
    
    def e2(self):
        l1_0 = ListNode(0)
        l2_0 = ListNode(0)

        return l1_0, l2_0
    
    def e3(self):
        l1_6 = ListNode(9)
        l1_5 = ListNode(9, l1_6)
        l1_4 = ListNode(9, l1_5)
        l1_3 = ListNode(9, l1_4)
        l1_2 = ListNode(9, l1_3)
        l1_1 = ListNode(9, l1_2)
        l1_0 = ListNode(9, l1_1)

        l2_3 = ListNode(9)
        l2_2 = ListNode(9, l2_3)
        l2_1 = ListNode(9, l2_2)
        l2_0 = ListNode(9, l2_1)

        return l1_0, l2_0

main = Main()
main.exec()