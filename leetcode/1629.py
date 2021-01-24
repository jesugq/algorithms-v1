from typing import List

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        release_times: List[int] = releaseTimes
        duration_times: List[int] = []
        previous_time: int = 0
        
        for i in range(len(release_times)):
            duration_times.append(release_times[i] - previous_time)
            previous_time = release_times[i]

        keys_pressed: str = keysPressed
        longest_time: int = 0

        for i in range(len(duration_times)):
            if duration_times[i] >= longest_time:
                longest_time = duration_times[i]

        longest_keys: List[str] = []

        for i in range(len(duration_times)):
            if duration_times[i] == longest_time:
                longest_keys.append(keys_pressed[i])
        longest_keys.sort(reverse=True)
        return longest_keys[0]

class Main:
    def exec(self):
        solution = Solution()
        release_times, keys_pressed = self.ex4()
        answer = solution.slowestKey(release_times, keys_pressed)
        print(answer)

    def ex1(self):
        return [9,29,49,50], "cbcd"

    def ex2(self):
        return [12,23,36,46,62], "spuda"

    def ex3(self):
        return [1,2], "ba"

    def ex4(self):
        return [1,2,3], "aba"

main = Main()
main.exec()