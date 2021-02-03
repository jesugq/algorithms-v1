class Solution:
    def dayOfYear(self, date: str) -> int:
        normal_days_per_month = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        leap_days_per_month =   [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
        date_year: int =  int(date[0:4] )
        date_month: int = int(date[5:7] )
        date_day: int =   int(date[8:10])

        cumulative_days_per_month = normal_days_per_month
        if date_year % 4 == 0:
            if date_year % 100 == 0:
                if date_year % 400 == 0:
                    cumulative_days_per_month = leap_days_per_month
            else:
                cumulative_days_per_month = leap_days_per_month
        date_day_of_year = cumulative_days_per_month[date_month - 1] + date_day
        return date_day_of_year

class Main:
    def execute(self):
        solution = Solution()
        tests = self.tests()
        for test in tests:
            answer = solution.dayOfYear(test[1])
            print(answer == test[0], answer)
    
    def tests(self):
        return [
            [9, '2019-01-09'],
            [41, '2019-02-10'],
            [60, '2003-03-01'],
            [61, '2004-03-01'],
            [31, '1700-01-31'],
            [59, '1700-02-28'],
            [60, '1600-02-29'],
            [60, '1700-03-01'],
            [61, '1600-03-01'],
            [90, '1700-03-31'],
            [91, '1600-03-31'],
            [365, '1700-12-31'],
            [366, '1600-12-31'],
        ]

main = Main()
main.execute()