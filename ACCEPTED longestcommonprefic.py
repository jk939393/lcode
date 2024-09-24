from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length_element = min(strs, key=len)
        count = 0
        val = 'false'
        prev = ""
        str = ""
        for i in range(len(min_length_element)):


            for z in range(len(strs)):
                prev = strs[z - 1][i]

                if prev != strs[z][i]:
                    val = 'true'
                    break

                print(strs[z][i],"currentVal")
                print(prev,"prev")

            if prev == strs[z][i] and val == 'false':
                count = count + 1
                str =  str + strs[z][i]
            print("count",count)

            print("cluster")
        if count == 0:
            return ""
        return str


#strs = ["dog","racecar","car"]

sol = Solution()
s =sol.longestCommonPrefix(["11og z","f2og z","fl"])
print(s,"return value")