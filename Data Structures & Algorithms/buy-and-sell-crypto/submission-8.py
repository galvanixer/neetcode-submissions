class Solution:
    # > Brute Force Solution: time: O(n^2), space: O(1)
    def maxProfit(self, prices: List[int]) -> int:

        nprices = len(prices)
        maxprofit = 0
        
        for i in range(nprices):
            for j in range(i+1, nprices):
                maxprofit = max(maxprofit, prices[j]-prices[i])

        return maxprofit


        