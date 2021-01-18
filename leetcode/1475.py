from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        payout = []
        length = len(prices)

        for i in range(length):
            j = i + 1
            current_price = prices[i]
            discount = 0
            while (j < length):
                potential_discount = prices[j]
                if potential_discount <= current_price:
                    discount = potential_discount
                    break
                else:
                    j += 1
            payout.append(current_price - discount)
        return payout

class Main:
    def execute(self):
        solution = Solution()
        print(solution.finalPrices(self.e1()))
        print(solution.finalPrices(self.e2()))
        print(solution.finalPrices(self.e3()))
    
    def e1(self):
        return [8,4,6,2,3]

    def e2(self):
        return [1,2,3,4,5]

    def e3(self):
        return [10,1,1,6]

main = Main()
main.execute()