from typing import List
import bisect

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k: int = k
        self.nums: List[int] = sorted(nums)
        self.length: int = len(self.nums)
        self.k_index = self.length - self.k

    def add(self, val: int) -> int:
        bisect.insort(self.nums, val)
        self.length += 1
        self.k_index += 1
        return self.nums[self.k_index]

class Main:
    def execute(self):
        tests = self.tests()
        for test in tests:
            solution = KthLargest(test[0], test[1])
            for attempt in test[2]:
                answer = solution.add(attempt[1])
                print(attempt[0] == answer, attempt[0], answer, solution.nums)
            print()

    def tests(self):
        return [
            [5, [2,4,6,8,10], [[2,1], [3,3], [4,5], [5,7]]],
            [3, [4,5,8,2], [[4,3], [5,5], [5,10], [8,9], [8,4]]],
        ]

main = Main()
main.execute()