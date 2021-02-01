from typing import List
from typing import Set

class Solution:
    def sortString(self, s: str) -> str:
        string: str = s
        sorted_string: str = sorted(string)
        unique_string: List[str] = sorted(set(sorted_string))
        unique_counts: List[int] = [0] * len(unique_string)

        sorted_index: int = 0
        for unique_index, unique_char in enumerate(unique_string):
            while sorted_index < len(sorted_string) and unique_char == sorted_string[sorted_index]:
                unique_counts[unique_index] += 1
                sorted_index += 1

        answer: str = ''
        sorted_index: int = 0
        while sorted_index < len(sorted_string):
            for index in range(len(unique_string)):
                if unique_counts[index] > 0:
                    answer += unique_string[index]
                    unique_counts[index] -= 1
                    sorted_index += 1
            for index in reversed(range(len(unique_string))):
                if unique_counts[index] > 0:
                    answer += unique_string[index]
                    unique_counts[index] -= 1
                    sorted_index += 1
        return answer

class Main:
    def execute(self):
        solution = Solution()
        tests = self.tests()
        answers = self.answers()
        if len(tests) != len(answers):
            return
        for index in range(len(tests)):
            answer = solution.sortString(tests[index])
            print(answer == answers[index], answer)

    def tests(self):
        return [
            "aaaabbbbcccc",
            "rat",
            "leetcode",
            "ggggggg",
            "spo",
        ]

    def answers(self):
        return [
            "abccbaabccba",
            "art",
            "cdelotee",
            "ggggggg",
            "ops",
        ]

main = Main()
main.execute()