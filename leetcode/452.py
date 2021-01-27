from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        START = 0
        END = 1
        MIN_NUM = -2147483648

        sorted_points = sorted(points, key=lambda coords: coords[END])
        minimum_shots = 0
        last_shot_index = -2147483649

        for balloon in sorted_points:
            if last_shot_index < balloon[START]:
                minimum_shots += 1
                last_shot_index = balloon[END]
            # print('[', balloon[START], ',', balloon[END], ']', minimum_shots, last_shot_index)
        return minimum_shots

class Main:
    def exec(self):
        solution = Solution()
        inputs = self.exam()
        for points in inputs:
            answer = solution.findMinArrowShots(points)
            print(answer)

    def exam(self):
        return [
                [[10,16],[2,8],[1,6],[7,12]],
                [[1,2],[3,4],[5,6],[7,8]],
                [[1,2],[2,3],[3,4],[4,5]],
                [[1,2]],
                [[2,3],[2,3]],
                [[-2147483648,2147483647]]
               ]

main = Main()
main.exec()