from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        mylist = []
        print(len(nums))
        flag = True
        start = None

        if len(nums) == 1:
            print("entering loop")
            print(nums[0])
            mylist.append(str(nums[0]))  # No assignment needed
            print(mylist)
            return mylist
        for i in range(len(nums) - 1):

            if nums[i] + 1 == nums[i + 1]:
                if flag == True:
                    start = nums[i]
                    flag = False
                    print("start", start)
                print("continuing", nums[i])
                if nums[i+1] == nums[-1]:
                    print("sequential", start)
                    # mylist.append(start)
                    # mylist.append(nums[i - 1])
                    r = f"{start}->{nums[-1]}"
                    mylist.append(r)
                    print(r)

            if nums[i] + 1 != nums[i + 1]:
                print(start, "startval (stopping)")
                print("stopping", nums[i])
                print("appending")
                # mylist.append(start)
                # mylist.append(nums[i - 1])
                print("test",start,nums[i])
                if start == nums[i]:
                    r = f"{start}"
                elif i == 0:
                    r = f"{nums[i]}"
                else:
                    r = f"{start}->{nums[i]}"
                mylist.append(r)
                print(r)

                start = nums[i + 1]
                print("newstart", start)
                flag = True
                if start == nums[-1]:
                    print("notsequential",start)
                    mylist.append(f'{start}')
        return mylist

nums = [-1]
# Output: ["0->2","4->5","7"]
sol= Solution()
a = sol.summaryRanges(nums)
print(a)