import typing

class UniqueFrequency:
    NO_LUCKY_INTEGER = -1
    INITIAL_FREQUENCY = 0
    
    VALUE_NOT_FOUND_INDEX = 'Value not found!'

    def __init__(self):
        self.unique_numbers = []
        self.unique_frequency = []
    
    def populate(self, common_numbers: typing.List[int]):
        self.create_unique_numbers(common_numbers)
        self.sort_unique_numbers()
        self.create_unique_frequency()

    def create_unique_numbers(self, common_numbers: typing.List[int]):
        for number in common_numbers:
            if number not in self.unique_numbers:
                self.unique_numbers.append(number)
    
    def sort_unique_numbers(self):
        self.unique_numbers.sort()

    def create_unique_frequency(self):
        one = self.INITIAL_FREQUENCY
        length = len(self.unique_numbers)

        for index in range(length):
            self.unique_frequency.append(one)

    def increase_for(self, number: int):
        try:
            index = self.unique_numbers.index(number)
            self.unique_frequency[index] += 1
        except ValueError:
            print(self.VALUE_NOT_FOUND)
            pass

    def get_lucky_integer(self) -> int:
        lucky = self.NO_LUCKY_INTEGER
        length = len(self.unique_numbers)

        for index in range(length):
            number = self.unique_numbers[index]
            frequency = self.unique_frequency[index]

            if number == frequency:
                lucky = number

        return lucky

class Solution:
    def findLucky(self, arr: typing.List[int]) -> int:
        return self.lucky_integer(arr)

    def lucky_integer(self, common_numbers: typing.List[int]) -> int:
        unique_numbers = UniqueFrequency()
        unique_numbers.populate(common_numbers)

        for number in common_numbers:
            unique_numbers.increase_for(number)
        
        return unique_numbers.get_lucky_integer()

class Main:
    def execute(self):
        solution = Solution()
        arr = self.example_two()

        answer = solution.findLucky(arr)
        print(answer)

    def example_one(self):
        return [2, 2, 3, 4]

    def example_two(self):
        return [1, 2, 2, 3, 3, 3]

    def example_three(self):
        return [2, 2, 2, 3, 3]
    
    def example_four(self):
        return [5]
    
    def example_five(self):
        return [7, 7, 7, 7, 7, 7, 7]

    def example_empty(self):
        return []

main = Main()
main.execute()