class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Max profit = Lowest price, highest sale

        lowestPrice = float('inf')
        maxProfit = 0

        for i in range(len(prices)):
            price = prices[i]

            if (price < lowestPrice):
                lowestPrice = price

            else:
                profit = price - lowestPrice

                if (profit > maxProfit): maxProfit = profit



        return maxProfit