class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Brute Force Solution
        # days = len(prices)
        # max_profit = 0

        # for l in range(days):
        #     for r in range(l + 1, days):
        #         profit = prices[r] - prices[l]
        #         max_profit = max(max_profit, profit if profit > 0 else 0)

        # return max_profit

        # O(n) solution

        lowest_buy = prices[0]
        highest_profit = 0

        for p in prices:
            highest_profit = max(highest_profit, p - lowest_buy)
            lowest_buy = min(p, lowest_buy)
        return highest_profit
            

