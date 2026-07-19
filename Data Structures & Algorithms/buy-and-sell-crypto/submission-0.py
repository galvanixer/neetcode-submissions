class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1. Brute Force Solution
        maxprofit = 0
        nprices = len(prices)
        for i in range(nprices):
            for j in range(i, nprices):
                tempdiff = prices[j] - prices[i]
                maxprofit = max(maxprofit, tempdiff)

        return maxprofit

