class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxProfit = 0

        for price in prices:
            maxProfit = max(maxProfit, price - minBuy)
            minBuy = min(minBuy, price)

        return maxProfit