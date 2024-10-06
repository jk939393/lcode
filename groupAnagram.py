from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mydict = {}
        for i in range(len(strs)):
            a= ''.join( sorted(strs[i]))
            print(a)
            if a not in mydict:
                mydict[a] = []
                mydict[a].append(strs[i])
            print(mydict)


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

sol = Solution()
sol.groupAnagrams(strs)