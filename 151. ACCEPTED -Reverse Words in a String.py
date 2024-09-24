class Solution:
    def reverseWords(self, s: str) -> str:
        s =s.split()
        z = ""
        print(s)
        for i in range(len(s)-1,-1,-1):
            print(s[i])
            z= " " + str(z) + s[i] + " "
        z = z.strip()
        return z
s = "  hello world  "
sol = Solution()
x = sol.reverseWords(s)
print(x)

