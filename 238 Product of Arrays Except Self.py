from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r= nums.copy()
        prefix = [nums[0]]
        postfix = []
        suffix = nums


        #left
        for i in range(len(nums)):
            if i > 0:
                print(nums[i])
                prefix.append(prefix[i -1] * nums[i])
        print(prefix)
        for i in range(len(nums) - 1, -1, -1):
            if i < 3:
                print(i)

                # print(nums[i])
                # #print(suffix[i])
                suffix[i] = (suffix[i+1] * nums[i])


        print(suffix)
        answer = []
        for i in range(len(nums)):
            pass
        for i in range(len(nums)):
            if i == 0:
                answer.append(suffix[i+1])
            #print(answer)
            if i > 0 and i < (len(nums)-1):

                answer.append(prefix[i-1] *suffix[i+1])
            print(answer)
            if i == len(nums)-1:
                answer.append(prefix[i-1])
            print(answer)
        return answer



sol = Solution()
sol.productExceptSelf([-1,1,0,-3,3])
#sol.productExceptSelf([-1,1,0,-3,3])

