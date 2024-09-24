class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        z = 0
        n= 0
        for i in range(len(haystack)):
            for i in range(len(needle)):
                if needle[i] ==haystack[i+n]:
                    print("Match found",i,"haystack:",haystack[i+n],"needle:",needle[i],"  z:",z)

                if needle[i] != haystack[i+n]:
                    print("NOT match",i,"haystack:",haystack[i+n],"needle:",needle[i],"  z",z)
            z = z +1

#

needle = "sad"
haystack = "szdbutsad"
sol = Solution()
sol.strStr(haystack,needle)