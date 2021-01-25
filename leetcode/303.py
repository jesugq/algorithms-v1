from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.numbers = nums

    def sumRange(self, i: int, j: int) -> int:
        total_sum = 0
        desired_range = range(i, j+1)

        for index in desired_range:
            total_sum += self.numbers[index]
        
        return total_sum

class Main:
    def e1(self):
        nums = [-2,0,3,-5,2,-1]
        solution = NumArray(nums)
        print(solution.sumRange(0,2))
        print(solution.sumRange(2,5))
        print(solution.sumRange(0,5))

main = Main()
main.e1()