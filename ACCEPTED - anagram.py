class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myDict = {}
        for i in range(len(s)):
            print((myDict))
            if s[i] in myDict:
                print("found in dic incr")
                myDict[s[i]] +=  1
            else:
                print("not in dict, set 1")
                myDict[s[i]] = 1

        print(myDict)

        #print(myDict)
        for i in range(len(t)):
            if t[i] in myDict:
                myDict[t[i]] -= 1
                print(myDict)
            if t[i] not in myDict:
                print("not in my dict")
                return False
            if myDict[t[i]] < 0:
                print("less than 1")
                return False
            if len(s) != len(t):
                return False
        return True

s = "aabbbb"
t= "aaaabb"

# s = "aacc"
# t = "ccac"
#
# s = "anagram"
# t = "nagaram"

sol = Solution()
a = sol.isAnagram(s,t)
print(a)