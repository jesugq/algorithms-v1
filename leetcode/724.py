import typing

class PivotFinder:
    NO_PIVOT_INDEX = -1
    NO_PIVOT_NUMBER = -1
    INITIAL_INDEX = 0
    INITIAL_VALUE = 0

    def __init__(self, numbers=None):
        self.numbers = numbers
        self.pivot_index = self.NO_PIVOT_INDEX
        self.pivot_number = self.NO_PIVOT_NUMBER

    def find_pivot(self) -> int:
        left_side_sum = self.INITIAL_VALUE
        right_side_sum = sum(self.numbers)
        previous_number = self.INITIAL_VALUE
        current_number = self.INITIAL_VALUE

        for index, number in enumerate(self.numbers):
            current_number = number
            left_side_sum += previous_number
            right_side_sum -= current_number
            
            if left_side_sum == right_side_sum:
                self.make_pivot(index, number)
                break
                
            previous_number = current_number

    def make_pivot(self, index: int, number: int) -> int:
        self.pivot_index = index
        self.pivot_number = number

    def get_pivot_index(self) -> int:
        return self.pivot_index

    def get_pivot_number(self) -> int:
        return self.pivot_number

class Solution:
    def pivotIndex(self, nums: typing.List[int]) -> int:
        pivot_finder = PivotFinder(nums)
        pivot_finder.find_pivot()
        return pivot_finder.get_pivot_index()

class Main:
    def execute(self):
        solution = Solution()
        nums = self.one()
        answer = solution.pivotIndex(nums)
        print(answer)

    def one(self):
        return [1,7,3,6,5,6]
    
    def two(self):
        return [1,2,3]

main = Main()
main.execute()