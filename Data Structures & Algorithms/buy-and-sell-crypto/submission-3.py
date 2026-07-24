class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0 
        lowest, r= 0 ,0

        for i in range(len(prices)):
            if prices[lowest] < prices[i]:
                total =  max(total, (prices[i]- prices[lowest]))
            if prices[lowest] > prices[i]:
                lowest= i

            
        return total



        