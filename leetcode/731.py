from typing import List
import bisect

class MyCalendarTwo:
    def __init__(self):
        self.calendar: List[List[int]] = []
        self.overlaps: List[List[int]] = []

    def book(self, start: int, end: int) -> bool:
        for overstart, overend in self.overlaps:
            if start < overend and end > overstart:
                return False
        for calstart, calend in self.calendar:
            if start < calend and end > calstart:
                self.overlaps.append([max(start, calstart), min(end, calend)])
        self.calendar.append([start, end])
        return True

class Main:
    def execute(self):
        tests = self.tests()
        answers = self.answers()
        for index in range(len(tests)):
            test = tests[index]
            answer = answers[index]
            solution = MyCalendarTwo()
            for single_index in range(len(test)):
                single_test = test[single_index] 
                single_answer = answer[single_index] 
                single_output = solution.book(single_test[0], single_test[1])
                print(single_answer == single_output, '|', single_answer, single_output)
            print()
    
    def tests(self):
        return [
            [[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]],
            [[26,35],[26,32],[25,32],[18,26],[40,45],[19,26],[48,50],[1,6],[46,50],[11,18]],
            [[5,12],[42,50],[4,9],[33,41],[2,7],[16,25],[7,16],[6,11],[13,18],[38,43],[49,50],[6,15],[5,13],[35,42],[19,24],[46,50],[39,44],[28,36],[28,37],[20,29],[41,49],[11,19],[41,46],[28,37],[17,23],[22,31],[4,10],[31,40],[4,12],[19,26]]
        ]
    def answers(self):
        return [
            [True,True,True,False,True,True], 
            [True,True,False,True,True,True,True,True,True,True], 
            [True,True,True,True,False,True,False,False,True,True,True,False,False,False,True,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False],
        ]

main = Main()
main.execute()