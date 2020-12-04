import typing
import math

class SampledStatistics:    
    NO_SAMPLE_COUNT = 0

    def __init__(self, sample_count: typing.List[int]):
        self.sample_count = sample_count
        self.sample_total = None

        self.minimum = None
        self.maximum = None
        self.mean = None
        self.median = None
        self.mode = None

    def initialize(self):
        self.make_sample_total()

        self.calculate_minimum()
        self.calculate_maximum()
        self.calculate_mean()
        self.calculate_median()
        self.calculate_mode()

    def make_sample_total(self):
        self.sample_total = 0

        for number in self.sample_count:
            if number > self.NO_SAMPLE_COUNT:
                self.sample_total += number

    def calculate_minimum(self):
        indexed_count = enumerate(self.sample_count)

        for index, number in indexed_count:
            if number > self.NO_SAMPLE_COUNT:
                self.minimum = index
                break

    def calculate_maximum(self):
        reversed_count = reversed(list(enumerate(self.sample_count)))

        for index, number in reversed_count:
            if number > self.NO_SAMPLE_COUNT:
                self.maximum = index
                break

    def calculate_mean(self):
        indexed_count = enumerate(self.sample_count)
        number_sum = 0.0

        for index, number in indexed_count:
            if number > self.NO_SAMPLE_COUNT:
                number_sum += index * number
        
        self.mean = number_sum / self.sample_total

    def calculate_median(self):
        if self.sample_total % 2 == 0:
            self.calculate_median_even()
        else:
            self.calculate_median_odd()

    def calculate_median_even(self):
        indexed_count = enumerate(self.sample_count)

        target = self.sample_total / 2
        target_one = math.floor(target)
        target_two = target_one + 1

        value = None
        value_one = None
        value_two = None
        
        total = 0

        for index, number in indexed_count:
            if number > self.NO_SAMPLE_COUNT:
                total += number

            if total >= target_one and value_one is None:
                value_one = index
            if total >= target_two and value_two is None:
                value_two = index
            
            if value_one is not None and value_two is not None:
                value = (value_one + value_two) / 2
                break
        
        self.median = value

    def calculate_median_odd(self):
        indexed_count = enumerate(self.sample_count)

        target = self.sample_total / 2
        value = None
        total = 0

        for index, number in indexed_count:
            if number > self.NO_SAMPLE_COUNT:
                total += number
            
            if total >= target:
                value = index
                break
        
        self.median = value

    def calculate_mode(self):
        indexed_count = enumerate(self.sample_count)

        mode = None
        mode_count = 0

        for index, number in indexed_count:
            if number > mode_count:
                mode = index
                mode_count = number

        self.mode = mode

class Solution:
    def sampleStats(self, count: typing.List[int]) -> typing.List[float]:
        sampledStatistics = SampledStatistics(count)
        sampledStatistics.initialize()
        
        answer = list()
        answer.append(sampledStatistics.minimum) 
        answer.append(sampledStatistics.maximum)
        answer.append(sampledStatistics.mean)
        answer.append(sampledStatistics.median)
        answer.append(sampledStatistics.mode)
        return answer

class Main:
    def execute(self):
        solution = Solution()
        count = self.two()

        answer = solution.sampleStats(count)
        print(answer)

    def one(self):
        return [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    def two(self):
        return [0,4,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

main = Main()
main.execute()