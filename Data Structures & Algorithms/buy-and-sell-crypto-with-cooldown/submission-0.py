class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]
        sold = 0
        cooldown = 0

        for price in prices[1:]:
            prev_hold = hold
            hold = max(hold, cooldown - price)
            cooldown = max(cooldown, sold)
            sold = prev_hold + price

        return max(sold, cooldown)