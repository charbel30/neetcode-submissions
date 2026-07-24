class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0 
        lowest= prices[0]

        for i in range(len(prices)):
            total =  max(total, (prices[i]- lowest))
            lowest = min(lowest, prices[i])
        return total



        