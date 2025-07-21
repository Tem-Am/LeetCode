class Solution:
    def maxProfit(self, prices):
        buy = 999999
        sell = 0
        for p in prices:
            # know when to sell
            if sell < p - buy:
                sell = p - buy
            if p < buy:
                buy = p
        return sell