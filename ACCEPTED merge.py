from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sort = sorted((intervals))
        # print(sort)
        # print(sort[0][1])
        i = 0
        print("sorted",sort)
        while i < len(sort)-1:
            if sort[i+1][0] <= sort[i][1]:
                sort[i][1] = max(sort[i][1], sort[i + 1][1])
                sort.pop(i + 1)

                print(sort[i][0],sort[i][1])
                print(sort)
            else:
                i = i + 1
        return sort
intervals = [[1, 3], [2, 6], [8, 10], [15, 18],[14, 18]]
#intervals = [[1,4],[0,2],[3,5]]

s = Solution()
a = s.merge(intervals)
print(a)