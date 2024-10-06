class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapst = {}
        mapts = {}
        for i in  range(len(s)):
            mapst[s[i]] = t[i]
            mapts[t[i]] = s[i]
            print(mapst)
            print(mapts)
            if s[i] in  mapst[s[i]] and s[i] != t[i]:
                return False
            if t[i] in mapts[t[i]] and t[i] != s[i]:
                return False
        return True




s = "egg"
t = "adz"
sol = Solution()
a =sol.isIsomorphic(s,t)
print(a)

