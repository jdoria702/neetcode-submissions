class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        buy = prices[0]
        profit = 0
        while r < len(prices):
            if prices[r] - buy > profit:
                profit = prices[r] - buy

            if prices[r] < buy:
                buy = prices[r]
                l = r
            
            r = r + 1
        
        return profit