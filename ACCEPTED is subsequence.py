class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        z= 0
        if s== "" and t=="":
            return True
        while i < len(t):

            print("z",z,"i",(i))

            if i == len(s):
                print("true")
                return True
            if z == len(t):
                print("false")
                return False

            if s[i] == t[z]:
                print("match",s[i],t[z],"z:",z,"i",i)
                z = z + 1
                i = i + 1
                print(len(s))

                continue
            else:
                print("not match",s[i],t[z])
                z = z + 1






sol = Solution()

s = "dc"
t = "ahbgdc"
sol.isSubsequence(s,t)