class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        myDict = {}
        for i in range(len(magazine)):
            print(magazine[i])
            if magazine[i] in myDict:
                myDict[magazine[i]] += 1
            else:
                 myDict[magazine[i]] = 1
        print(myDict)
        for i in range(len(ransomNote)):
            print(("ransomeNote[i]",ransomNote[i]))
            if ransomNote[i] in myDict:
                myDict[ransomNote[i]] -= 1
            if ransomNote[i] not in myDict:
                return False
            if myDict[ransomNote[i]] == -1:
                return False


        print(myDict)

        return True


sol = Solution()

ransomNote = "a"
magazine = "b"
result = sol.canConstruct(ransomNote, magazine)

print(result)
