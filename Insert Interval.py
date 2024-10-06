from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        sort = sorted(intervals)
        while i < len(sort)-1:
            if newInterval[0] <= sort[i][1]:
                intervals[i][1] = max(newInterval[0],intervals[i][1])
                print(intervals)
                intervals.pop(i+1)
            else:
                i = i + 1

intervals = [[1,3],[6,9]]
newInterval = [2,5]

# intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
# newInterval = [4, 8]
sol = Solution()
a = sol.insert(intervals,newInterval)
print(a)