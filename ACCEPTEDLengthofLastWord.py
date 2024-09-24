from typing import Any


class Solution:
    def lengthOfLastWord(self, s: str) -> int | str | Any:
        flag = False
        count = 0
        if len(s) == 1:
            return 1
        z =0
        for i in range(len(s) - 1, -1, -1):
            z = z + 1
            print("iterate")
            #print(len(s))
            if len(s) == 2 and s[1] == " ":
               # print("len2")
                return 1

            # if len(s) == -1:
            #     return 1

            if s[i] != " ":
                print("not space")
                flag = True
                count = count + 1
                print(count)
                print(z,len(s))
            if z == len(s):
                return count
           # print(s[i], i)
            #print(flag)
            if s[i] == " " and flag == True:
                print("Exiting")
                return (count)

            if count == len(s):
                return count



sol = Solution()
s= sol.lengthOfLastWord("day    ")
print(s)
