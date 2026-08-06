class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Brute Force Solution
        days = len(prices)
        max_profit = 0

        for l in range(days):
            for r in range(l + 1, days):
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit if profit > 0 else 0)

        return max_profit

