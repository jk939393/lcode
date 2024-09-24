from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totalprofit = 0
        currentprofit = 0
        for i in range(len(prices)-1):
            #print(prices[i])
            if (prices[i+1] - prices[i]) > 0:
                currentprofit = prices[i+1] - prices[i]
                totalprofit = currentprofit +totalprofit

                print(currentprofit)
        return totalprofit




sol = Solution()
a= sol.maxProfit([7,1,5,3,6,4])
#a sol.maxProfit([1,2,3,4,5])

print(a)

