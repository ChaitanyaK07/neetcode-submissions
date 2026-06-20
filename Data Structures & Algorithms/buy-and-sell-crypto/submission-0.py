class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min = prices[0]
        max_price = 0

        for i in prices:

            if i < min:
                min = i
            elif i-min > max_price:
                max_price = i - min

        return max_price
        