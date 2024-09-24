from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        length = min(len(nums1), len(nums2))

        for i in range(length):

            if nums1[i] <= nums2[i]:
                nums1[i] = nums1[i]
                print(nums1[1])
            else:
                nums1[i] = nums2[i]
                print(nums1[1])
        print(nums1)



if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]  # Example list 1
    m = 3                         # Number of elements in nums1 to consider
    nums2 = [2, 5, 6]             # Example list 2
    n = 3                         # Number of elements in nums2

    solution = Solution()         # Create an instance of the Solution class
    solution.merge(nums1, m, nums2, n)  # Call the merge method

    print(nums1)  # Output the modified nums1 lis