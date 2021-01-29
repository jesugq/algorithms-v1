from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums: List[int] = sorted(nums)
        
        first = 0
        last = len(sorted_nums) - 1
        left = first
        right = last

        while (right != first):
            value_left = sorted_nums[left]
            value_right = sorted_nums[right]
            combo = value_left + value_right

            if combo == target:
                answer = []
                for index, num in enumerate(nums):
                    if num == value_left or num == value_right:
                        answer.append(index)
                return answer
                
            elif combo > target:
                last -= 1
                left = first
                right = last
            else:
                left += 1
        return [-1, -1]

class Main:
    def exec(self):
        solution = Solution()
        for input in self.exam():
            print(solution.twoSum(input[0], input[1]))
    
    def exam(self):
        return [
            [[2,7,11,15], 9],       # [0,1]
            [[3,2,4], 6],           # [1,2]
            [[3,3], 6],             # [0,1]
            [[-3,4,3,90], 0],       # [0,2]
            [[-1,-2,-3,-4,-5], -8]  # [2,4]
        ]

main = Main()
main.exec()