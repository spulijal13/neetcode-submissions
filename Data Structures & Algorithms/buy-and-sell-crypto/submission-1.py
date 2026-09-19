class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        minimum_buy = prices[0]

        for s in prices:
            max_profit = max(max_profit, s - minimum_buy)
            minimum_buy = min(minimum_buy, s)

        return max_profit