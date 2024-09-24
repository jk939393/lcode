from typing import List


class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        canidate = 0
        count = 0

        i=  0
        while i < len(nums):
            if len(nums) == 1:
                return nums[i]
            if nums[i-1] != nums[i] and nums[i] > 0:
                print("path")
                count = count + 1
                canidate = nums[i]
            else:
                print("path1")
                count = count -1
                canidate = nums[i]

            i = i+1
        return canidate



solution = Solution() #create object
result = solution.majorityElement([2,2]) # call thethod from the instaniaed objecct return as integer
print(result)
