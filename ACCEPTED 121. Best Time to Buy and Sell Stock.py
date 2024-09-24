from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        r = 0

        for i in range(len(prices)):
            #print(prices[i])
            if prices[i] < min_price:
                min_price = prices[i]
            #print(min_price)
            if (prices[i] - min_price) > r:
                r = (prices[i]-min_price)
            print(r)
        return r






sol = Solution()
a= sol.maxProfit([7,1,5,3,6,4])
print(a)