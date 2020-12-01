import typing

class PivotFinder:
    NO_PIVOT_INDEX = -1
    NO_SINGLE_SUM = 0

    def __init__(self, numbers=None):
        self.numbers = numbers
        self.length = len(numbers)
    
    def find_pivot_index(self) -> int:
        for index, number in enumerate(self.numbers):
            if self.sides_are_equal(index):
                return index
        return self.NO_PIVOT_INDEX
        

    def sides_are_equal(self, index: int) -> bool:
        left_sum = self.sides_left_sum(index)
        right_sum = self.sides_right_sum(index)

        return left_sum == right_sum

    def sides_left_sum(self, index: int) -> int:
        start = 0
        stop = index

        if start >= stop:
            return self.NO_SINGLE_SUM
        else:
            return self.sides_single_sum(start, stop)
    
    def sides_right_sum(self, index: int) -> int:
        start = index + 1
        stop = self.length

        if start >= stop:
            return self.NO_SINGLE_SUM
        else:
            return self.sides_single_sum(start, stop)

    def sides_single_sum(self, start: int, stop: int) -> int:
        single_sum = 0
        for index in range(start, stop):
            single_sum += self.numbers[index]
        return single_sum

class Solution:
    def pivotIndex(self, nums: typing.List[int]) -> int:
        pivot_finder = PivotFinder(nums)
        return pivot_finder.find_pivot_index()

class Main:
    def execute(self):
        solution = Solution()
        nums = self.two()
        answer = solution.pivotIndex(nums)
        print(answer)

    def one(self):
        return [1,7,3,6,5,6]
    
    def two(self):
        return [1,2,3]

main = Main()
main.execute()