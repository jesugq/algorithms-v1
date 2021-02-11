from typing import List

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        alls: List[int] = A
        evens: List[int] = []
        odds: List[int] = []
        answer: List[int] = []

        for number in alls:
            if number % 2 == 0:
                evens.append(number)
            else:
                odds.append(number)
        
        length: int = len(evens)
        for index in range(length):
            answer.append(evens[index])
            answer.append(odds[index])
        
        return answer

class Main:
    def execute(self):
        solution = Solution()
        tests = self.tests()
        for test in tests:
            answer = solution.sortArrayByParityII(test[1])
            print(test[0] == answer, test[0], answer)
    
    def tests(self):
        return [
            [[4,5,2,7], [4,2,5,7]],
            [[8,1,2,7,4,9,8,3], [8,1,2,4,7,9,3,8]],
        ]

main = Main()
main.execute()