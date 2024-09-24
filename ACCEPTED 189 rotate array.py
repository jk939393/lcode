from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

       # print(len(nums))
        #print(nums[len(nums)-1])
        k = k % len(nums)
        x = 0
        a = []
        z = k
        print(nums[len(nums)-1])
        for i in range(len(nums) - 1, 0, -1):
            # print(nums[i])
            z = z -1
            print(z)
            if z >= 0:
                print("append")
                a.append(nums[i])
                print(nums[i])
            nums[i] = nums[i-k]
            print(a)

        for i in range(len(a)):
            nums[i] = a[-(i + 1)]
        print(nums)






Solution = Solution()

Solution.rotate( [1,2,3,4,5,6,7],3)

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]