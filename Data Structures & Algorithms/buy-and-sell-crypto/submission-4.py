class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        days = len(prices)
        max_profit = 0
        l, r = 0, 1

        for l in range(days):
            for r in range(l, days):
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit if profit > 0 else 0)

        return max_profit