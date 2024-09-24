from typing import List



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
nums = [1, 1,1, 2,3,4,4,5,6,7,7,7,7,8]
counter = 0
for i in range(len(nums) - 1, 0, -1):
    print(i)

    if nums[i - 1] == nums[i]:
        counter = counter + 1
        if counter >= 2:
            print("counter " + str(counter) + " val " + str(nums[i]))
            del nums[i]
    else:
        counter= 0
print(nums)

        # print("dup" + str(nums[i]))
        # del nums[i]
