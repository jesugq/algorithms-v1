import numpy
import typing

class Candies:
    NO_CANDIES = 0
    INITIAL_CANDY_PER_TURN = 1
    INCREASE_CANDY_PER_TURN = 1

    def __init__(self,
        candies_giveaway = NO_CANDIES,
        candies_per_turn = INITIAL_CANDY_PER_TURN,
        candies_left = NO_CANDIES
    ):
        self.candies_giveaway = candies_giveaway
        self.candies_per_turn = candies_per_turn
        self.candies_left = candies_left

    def emptied(self) -> bool:
        return self.candies_left == self.NO_CANDIES

    def prepare(self):
        self.candies_giveaway = min(self.candies_per_turn, self.candies_left)
        self.candies_per_turn += self.INCREASE_CANDY_PER_TURN
        self.candies_left -= self.candies_giveaway

    def take(self) -> int:
        candies_taken = self.candies_giveaway
        self.candies_giveaway = self.NO_CANDIES
        return candies_taken

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> typing.List[int]:
        candies_object = Candies(candies_left=candies)
        return self.increasing_candies(candies_object, num_people)

    def increasing_candies(self, candies: Candies, people_count: int) -> typing.List[int]:
        index = self.create_index()
        people_candies = self.create_peoples_candies(people_count)

        while not candies.emptied():
            candies.prepare()
            people_candies[index] += candies.take()
            index = self.move_index(index, people_count)

        return people_candies

    def create_index(self) -> int:
        return 0
    
    def create_peoples_candies(self, people_count: int) -> typing.List[int]:
        return numpy.zeros(people_count, dtype=int)

    def move_index(self, index: int, people_count: int) -> int:
        if index + 1 == people_count:
            return 0
        else:
            return index + 1

class Main:
    def execute(self):
        solution = Solution()
        candies, num_people = self.example_two()
        answer = solution.distributeCandies(candies, num_people)
        print(answer)

    def example_one(self):
        return 7, 4
    
    def example_two(self):
        return 10, 3

main = Main()
main.execute()