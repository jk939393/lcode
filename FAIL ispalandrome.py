class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True
        s = s.lower()
        i = 0
        for z in range(len(s) - 1, -1, -1):
            if not s[z].isalnum():
                continue
            if not s[i].isalnum():
                i += 1
                continue

            if s[z] != s[i]:
                print("not palindrome")
                return False

            i += 1

            if z <= i:  # Stop if pointers cross or meet
                break

        print("palindrome")
        return True


s = "A man, a plan, a canal: Panama"
sol = Solution()
sol.isPalindrome(s)