from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = numbers
        t = target
        i = 1
        z= 0
        mydict = {}


        while i < len(n):
            print(i,z)
            mydict[i] =t -n[i]
            print(mydict)
            if n[i]+ n[z] == t:
                print("true")
                a = [z,i]
                return a

            i = i + 1
            if i == len(n):
                print("z","incrementing z index", )
                z = z + 1
                i = z + 1
        print("false")



n =numbers = [2, 7, 10, 12]

t = target = 22


sol = Solution()
s = sol.twoSum(n,t)
print(s)
