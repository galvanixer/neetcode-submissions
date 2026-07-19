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
        # maxprofit = 0
        # tempbuy = prices[0]
        # for i in range(1, len(prices)):
        #     if prices[i] < tempbuy:
        #         tempbuy = prices[i]
        #     tempdiff = prices[i] - tempbuy
        #     maxprofit = max(maxprofit, tempdiff)

        # return maxprofit

        # 3. Dynamic Programming
        if len(prices)==0:
            return 0

        minbuy = prices[0]
        maxprofit = 0
        for price in prices:
            minbuy = min(minbuy, price)
            maxprofit = max(maxprofit, price-minbuy)

        return maxprofit




