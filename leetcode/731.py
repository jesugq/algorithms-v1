from typing import List
import bisect

class MyCalendarTwo:
    def __init__(self):
        self.START: int = 0
        self.END: int = 1
        self.books: List[List[int]] = []

    def book(self, start: int, end: int) -> bool:
        possible = self.possible_booking(start, end)
        if possible:
            self.add_booking(start, end)
            return True
        return False

    def possible_booking(self, start: int, end: int):
        relevant_books: List[List[int]] = [[start, end]]
        relevant_times: Set[int] = set([start, end])
        for book in self.books:
            if book[self.END] < start:
                continue
            elif start <= book[self.START] or start < book[self.END] or book[self.START] < end or book[self.END] <= end:
            # elif start <= book[self.START] or book[self.START] < end or start < book[self.END] or book[self.END] <= end:
                relevant_books.append(book)
                relevant_times.add(book[self.START])
                relevant_times.add(book[self.END])
            elif book[self.START] > end:
                break
        
        for time in relevant_times:
            times_repeated: int = 0
            for book in relevant_books:
                if book[self.START] <= time < book[self.END]:
                    times_repeated += 1
                if times_repeated > 2:
                    return False
        return True

    def add_booking(self, start: int, end: int):
        bisect.insort(self.books, [start,end])

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
                print(single_answer == single_output, '|', single_answer, single_output, solution.books)
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