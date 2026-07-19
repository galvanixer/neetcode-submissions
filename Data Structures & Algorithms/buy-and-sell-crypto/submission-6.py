class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # # 1. Brute Force Solution
        # maxprofit = 0
        # nprices = len(prices)
        # for i in range(nprices):
        #     for j in range(i, nprices):
        #         tempdiff = prices[j] - prices[i]
        #         maxprofit = max(maxprofit, tempdiff)

        # return maxprofit

        # 2. A little smarter solution (let's clean it a bit.)
        maxprofit = 0
        tempbuy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < tempbuy:
                tempbuy = prices[i]
            tempdiff = prices[i] - tempbuy
            maxprofit = max(maxprofit, tempdiff)

        return maxprofit

