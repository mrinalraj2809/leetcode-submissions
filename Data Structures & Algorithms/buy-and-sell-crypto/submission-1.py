class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_max = 0

        for i in range(len(prices)-1):
            
            for j in range(i, len(prices)):
                recover_prices = prices[j] - prices[i]
                profit_max = recover_prices if recover_prices > profit_max else profit_max
        return profit_max
                    