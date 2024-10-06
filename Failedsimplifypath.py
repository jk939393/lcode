class Solution:

    def simplifyPath(self, path: str) -> str:
        stack= []
        z = 0
        i = 0
        flag = False
        count = 0
        while z < len(path):
            print("ival",i)
            if flag == False:
                i = path[z]
            if stack:
                print(stack[-1],"stack-1","z",z,"lenpath",len(path)-1)
                if i == "/" and stack[-1] == "/" :
                    print("continue")
                    z= z+1
                    continue
                else:
                    print("append non empty stack")
                    stack.append(i)
                    print(stack)
                    print(stack[-1], "stack-1", "i", i, "lenpath", len(path))

                    if stack[-1] == "." and i == "." and flag== False:
                        print(stack[-1], "stack-1", "i", i, "lenpath", len(path))

                        flag = True

                        print("double period")
                        print("Test",flag,count)
                    if flag == True and count <2:
                        print("flag truepopping ..")
                        stack.pop()
                        print(stack)


                        if stack[-1] == "/" and count ==0:
                            print("first slash")
                            stack.pop()
                            print(stack)

                            count = 1
                        if count == 1:
                            print("count=1")
                            stack.pop()
                            print(stack)

                        if stack[-1] == "/" and count ==1:
                            print("flag false")
                            flag = False

                        #  stack.append(i)


                    if z == len(path)-1 and stack[-1] == "/":
                        print("lenpop")
                        stack.pop()
                        print(stack)

            else:
                print("append empty stack")
                stack.append(i)
                print(stack)

            z = z + 1
        print(stack)


#ath = "/home/"
#path = "/home//foo/"
path = "/home/user/Documents/../Pictures"
sol = Solution()
a= sol.simplifyPath(path)
print(a)

