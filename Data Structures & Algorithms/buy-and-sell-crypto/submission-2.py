class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mini = prices[0]

        max_profit = 0


        for i in prices:
            if i < mini:
                mini = i
            elif i - mini > max_profit:
                max_profit = i - mini

        return max_profit        