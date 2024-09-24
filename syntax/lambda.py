# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
add_3 = lambda z,y: z + z + 3 +y

v= add_3(4,0)
print(v)

nums = [(1,2),(2,1),(3,4)]

out2 = sorted(nums,key=lambda x: x[1] )

out = list(filter(lambda x: x*3==9,nums))

print(out2)

for i in range(len(nums) - 1, 0, -1):
    pass