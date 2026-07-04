class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        buy = float('inf')
        profit = 0
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
                continue
            if prices[i] > buy:
                profit = profit + prices[i] - buy
                buy = prices[i]
        
        return profit
