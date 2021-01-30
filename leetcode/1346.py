from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        zeroes = 0
        numbers = arr
        dictionary = {}
        for number in numbers:
            if number == 0:
                zeroes += 1
            else:
                dictionary[number] = True

        for number in numbers:
            if number * 2 in dictionary:
                return True
        if zeroes > 1:
            return True
        else:
            return False

class Main:
    def exec(self):
        solution = Solution()
        tests = self.test()
        for test in tests:
            print(solution.checkIfExist(test))

    def test(self):
        return [
            [10,2,5,3],             # True
            [7,1,14,11],            # True 
            [3,1,7,11],             # False
            [-2,0,10,-19,4,6,-8],   # False
            [0,0]                   # True
        ]

main = Main()
main.exec()