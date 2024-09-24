class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map0 = {}
        map1 = {}
        for idx in map0:
            map0[s[idx]] = idx

            if map1[idx] == map1[idx]:
                return True
            else:
                return False


