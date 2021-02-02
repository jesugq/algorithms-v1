from typing import List

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        max_base = max(x, y)
        min_base = min(x, y)
        sets = set()

        if max_base != 1 and min_base != 1:
            max_exponent = 0
            max_operation = 1
            while max_operation < bound:
                min_exponent = 0
                min_operation = 1
                both_operation = max_operation + min_operation
                
                while both_operation <= bound:
                    sets.add(both_operation)
                    min_exponent += 1
                    min_operation = pow(min_base, min_exponent)
                    both_operation = max_operation + min_operation

                max_exponent += 1
                max_operation = pow(max_base, max_exponent)
        elif max_base != 1 and min_base == 1:
            max_exponent = 0
            max_operation = 1
            while max_operation + 1 <= bound:
                sets.add(max_operation + 1)
                max_exponent += 1
                max_operation = pow(max_base, max_exponent)
        else:
            return [2] if bound >= 2 else []
        answer = sorted(sets)
        return answer

class Main:
    def execute(self):
        solution = Solution()
        tests = self.tests()
        answers = self.answers()
        if len(tests) != len(answers):
            return
        for index in range(len(tests)):
            answer = solution.powerfulIntegers(tests[index][0], tests[index][1], tests[index][2])
            print(answer == answers[index], answer)
    
    def tests(self):
        return [
            [2, 3, 10],
            [3, 5, 15],
            [2, 1, 10],
            [1, 2, 1000000],
            [1, 1, 1],
            [1, 1, 9999999],
        ]

    def answers(self):
        return [
            [2,3,4,5,7,9,10],
            [2,4,6,8,10,14],
            [2,3,5,9],
            [2,3,5,9,17,33,65,129,257,513,1025,2049,4097,8193,16385,32769,65537,131073,262145,524289],
            [],
            [2],
        ]

main = Main()
main.execute()