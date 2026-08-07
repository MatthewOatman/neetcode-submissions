class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Notes:

        Key word is future:

        Thus only dates in the later part are needed

        prices = [10, 1, 5, 3, 2]
        profit = 0

        because no further date after has the highest profit

        profit = sell - bought 
        '''
        profit = 0
        buy = prices[0]

        for sell in prices:
            profit = max(sell - buy, profit)
            buy = min(buy, sell)

        return profit

