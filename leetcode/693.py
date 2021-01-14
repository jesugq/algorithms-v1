class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        target = n
        iteration = 0
        aggregation = 1

        while target > iteration:
            iteration = iteration * 2 + aggregation
            if aggregation == 0: aggregation = 1
            else:                aggregation = 0
        
        return target == iteration

solution = Solution()
answer = solution.hasAlternatingBits(3)
print(answer)