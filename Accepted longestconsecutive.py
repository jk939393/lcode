from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Sort the input
        sort = sorted(set(nums))
        # print(sort)
        # print(len(sort))
        streak = 1
        maxStreak = 0
        # print("len",len(nums))
        if len(sort) == 1:
            return 1
        flag = False
        for i in range(len(sort)-1):

            print(sort[i],sort[i+1])

            if sort[i]+1 == sort[i+1]:
                flag = True
                streak = streak +1
                print("streak",streak)
                if streak > maxStreak:
                    maxStreak = streak
                    print("maxStreak",maxStreak)
            else:
                print("test")
                streak = 1
            if flag == False:
                maxStreak = 1

        return maxStreak
nums = [-6,-1,-1,9,-8,-6,-6,4,4,-3,-8,-1,0]

s = Solution()
a =s.longestConsecutive(nums)
print(a)