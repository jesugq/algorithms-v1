from typing import List

class SetBit:
    def __init__(self, number:int, bits_set:int):
        self.number = number
        self.bits_set = bits_set

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        numbers:List[int] = arr
        setbits:List[Setbit] = []
        answer:List[int] = []

        for number in numbers:
            binary:str = str(bin(number))
            bits_set:int = 0
            for digit in binary:
                if digit == '1':
                    bits_set += 1
            setbits.append(SetBit(number, bits_set))
        setbits.sort(key=lambda x : x.number)
        setbits.sort(key=lambda x : x.bits_set)
        
        for setbit in setbits:
            answer.append(setbit.number)
        return answer
        
class Main():
    def execute(self):
        solution = Solution()
        tests = self.tests()
        answers = self.answers()
        if len(tests) != len(answers):
            exit()
        for i in range(len(tests)):
            answer = solution.sortByBits(tests[i])
            print(answer == answers[i])

    def tests(self):
        return [
            [0,1,2,3,4,5,6,7,8],
            [1024,512,256,128,64,32,16,8,4,2,1],
            [10000,10000],
            [2,3,5,7,11,13,17,19],
            [10,100,1000,10000],
        ]

    def answers(self):
        return [
            [0,1,2,4,8,3,5,6,7],
            [1,2,4,8,16,32,64,128,256,512,1024],
            [10000,10000],
            [2,3,5,17,7,11,13,19],
            [10,100,10000,1000],
        ]

main = Main()
main.execute()