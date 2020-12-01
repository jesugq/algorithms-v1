class Solution:
    ONE = '1'

    def countAndSay(self, number: int) -> str:
        if self.numberIsOneOrLess(number):
            return self.ONE

        past = self.countAndSay(number - 1)
        return self.justSay(past)
        
    def numberIsOneOrLess(self, number: int) -> bool:
        return number <= 1

    def justSay(self, string: str) -> str:
        countOfCurrent = 0
        current = string[0]
        sequence = ''

        for i in range(len(string)):
            if current != string[i]:
                sequence += str(countOfCurrent) + str(current)
                current = string[i]
                countOfCurrent = 1
            else:
                countOfCurrent += 1
        sequence += str(countOfCurrent) + str(current)

        return sequence

solution = Solution()
answer = solution.countAndSay(4)
print(answer)