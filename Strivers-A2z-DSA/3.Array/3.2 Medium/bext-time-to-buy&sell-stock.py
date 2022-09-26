class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        min_v = min(prices[0], prices[1])
        max_p = prices[1] - prices[0]
        for i in range(2, len(prices)):
            if max_p < prices[i] - min_v:
                max_p = prices[i] - min_v
            min_v = min(min_v, prices[i])
        return max(0, max_p)



