class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        right = [0] * len(prices)
        maximum = -1
        for i in range(len(prices)-1, -1, -1):
            maximum = max(prices[i], maximum)
            right[i] = maximum
        maximum_profit = 0
        for i in range(len(prices)):
            recovered_profit = right[i] - prices[i]
            if recovered_profit > maximum_profit:
                maximum_profit = recovered_profit
        return maximum_profit
        # profit_max = 0

        # for i in range(len(prices)-1):
            
        #     for j in range(i, len(prices)):
        #         recover_prices = prices[j] - prices[i]
        #         profit_max = recover_prices if recover_prices > profit_max else profit_max
        # return profit_max
                    