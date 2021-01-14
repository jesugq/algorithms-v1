from typing import List

class Balloon:
    def __init__(self, number: int, start: int, end: int):
        self.number = number
        self.start = start
        self.end = end
        self.bursted = False

class Solution:
    def __init__(self):
        self.BALLOON_START = 0
        self.BALLOON_END = 1
        self.balloons = []

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        if len(points) == 1:
            return 1
        self.make_balloons(points)
        self.order_balloons()
        return self.minimum_shots_needed()

    def points_are_zero(self, points: List[List[int]]) -> bool:
        if len(points) == 0:
            return True

    def make_balloons(self, points: List[List[int]]):
        for index, coords in enumerate(points):
            self.balloons.append(Balloon(index, coords[self.BALLOON_START], coords[self.BALLOON_END]))

    def order_balloons(self):
        self.balloons.sort(key=lambda object: object.start)

    def minimum_shots_needed(self):
        minimum_shots = 0
        for balloon in self.balloons:
            if not balloon.bursted:
                aimed_position = self.position_most_bursts(balloon.start, balloon.end)
                self.burst_balloons_at(aimed_position)
                minimum_shots += 1
        return minimum_shots

    def burst_balloons_at(self, position: int):
        for balloon in self.balloons:
            if balloon.start <= position and balloon.end >= position :
                balloon.bursted = True

    def last_dense_shot_between(self, start: int, end: int) -> int:
        position = 0
        densest = self.killshots[position]
        for index in range(start, end + 1):
            if self.killshots[index] >= densest:
                position = index
                densest = self.killshots[position]
        return position

    def position_most_bursts(self, start_index: int, end_index: int) -> int:
        position = start_index
        highest_burst = 0
        for index in range(start_index, end_index + 1):
            bursts_at_index = 0
            for balloon in self.balloons:
                if balloon.start <= index and balloon.end >= index:
                    bursts_at_index += 1
            if bursts_at_index >= highest_burst:
                position = index
                highest_burst = bursts_at_index
        return position
            
class Main:
    def execute(self):
        solution = Solution()
        points = self.ex7()
        answer = solution.findMinArrowShots(points)
        print(answer)

    def ex1(self):
        return [[10,16],[2,8],[1,6],[7,12]]
    
    def ex2(self):
        return [[1,2],[3,4],[5,6],[7,8]]

    def ex3(self):
        return [[1,2],[2,3],[3,4],[4,5]]
    
    def ex4(self):
        return [[1,2]]

    def ex5(self):
        return [[2,3],[2,3]]

    def ex6(self):
        return [[1,2147483647]]

    def ex7(self):
        return [[-2147483646,-2147483645],[2147483646,2147483647]]

    def ex8(self):
        return [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]

main = Main()
main.execute()