from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            print(mydict)
            if target -complement in mydict:
                print("exit")
                c=i
                a = (mydict[target-complement])
                return [a, c]
            mydict[complement] = i





nums1 = [3,3]
target = 6
sol = Solution()

a= sol.twoSum(nums1,target)
print(a)