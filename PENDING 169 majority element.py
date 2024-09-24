from typing import List


class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        length = range(len(nums))
        counternew = 0
        max_count = 0
        maxvalue = 0
        for i in length:
            if i > 0 and nums[i] == nums[i - 1]:
                counternew = counternew + 1
                print(str(nums[i])+"same" + str(counternew))
                if counternew > max_count:
                    max_count = counternew
                    maxvalue = nums[i]
            if nums[i] != nums[i - 1]:
                counternew = 0
                counterprev = counternew
                print(str(nums[i])+"diff" + str(counterprev))
        return maxvalue



solution = Solution() #create object
result = solution.majorityElement([6,6,6,7,7]) # call thethod from the instaniaed objecct return as integer
print(result)
