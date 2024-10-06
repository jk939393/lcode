class Solution:
    def isValid(self, s: str) -> bool:
        dict = {")": "(", "}": "{", "]": "["}

        stack = []
        z= 0
        for i in s:
           # print(i)
           if stack:
                print(stack[-1])
           print(i)
           if i in dict:

                if stack and stack[-1] ==dict[i]:
                    print("dict match:", dict[i])
                    stack.pop()
                else:
                    stack.append(i)
                    print(stack)
                    print("1appending a")

           else:
                print("i not in dict")

                stack.append(i)
                print(stack)
                print("end")
           z = z + 1
           print("iteration",z)
        if not stack:
            print("stack", stack)
            return True


        else:
            print(stack)
            return False






s = "()[][]]]]"
Sol = Solution()
ans =Sol.isValid(s)
print(ans)