from typing import List

from range import length


# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         i = 0
#         for i in length(nums):
#             if nums[i+1] == nums[i]:
#                 nums[i+1] = nums[i+2]
#         #print(nums)
#
#
# # Instantiate the Solution class
# solution = Solution()
#
# # Define the input list
# nums = [1, 1, 2]
#
# Call the removeDuplicates method
# result = solution.removeDuplicates(nums)
#
# # Since there's no logic, result will be None
# print(result)  # Output: None
# nums = [1, 1, 2]
# i = 0
# for i in length(nums):
#     if nums[i + 1] == nums[i]:
#         nums[i + 1] = nums[i + 2]
#print(nums)