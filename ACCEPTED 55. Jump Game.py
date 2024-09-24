from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        index = -1
        flag = bool
        for n in range(len(nums)):

            # print(nums[-1])
            # print(len(nums)-1)
            # print(nums[4])

            a= nums[-1-n]
            index = index + 1
            print(a,index)
            if a>= index:
                index =0
            if a < index:
                flag = False
            else:
                flag = True
        return flag



sol = Solution()
#a= sol.canJump(nums = [2,3,1,1,4])
b= sol.canJump(nums = [10,0,1,0,0,0,1,4])

print(b)
