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

        # 2. A little smarter solution
        maxprofit = 0
        nprices = len(prices)
        tempbuy = prices[0]
        tempsell = prices[0]
        for i in range(1, nprices):
            if prices[i] < tempbuy:
                tempbuy = prices[i]
                tempsell = prices[i]
                print("Buy:", tempbuy)
            if (prices[i] > tempbuy) & (prices[i]>tempsell) :
                tempsell = prices[i]
                print("Sell:", tempsell)
            
            maxprofit = max(maxprofit, tempsell-tempbuy)

        return maxprofit

