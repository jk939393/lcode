nums1 = [1, 3, 5]
nums2 = [2, 4, 6, 8, 10]

length = max(len(nums1), len(nums2))
length = len(nums1)
print(range(length))

result = []
for i in range(length):
    if i < len(nums1):
        result.append(nums1[i])
    if i < len(nums2):
        result.append(nums2[i])

print(result)  # Output: [1, 2, 3, 4, 5, 6, 8, 10]