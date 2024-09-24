from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)
        max = citations[0:len(citations)]

        max.reverse()

        hindex = 0

        if len(max) == 0:
            return 1

        for z in range(len(max)):
            counter = 0

            for i in range(len(citations)):
                if citations[i] >= max[z]:
                    counter += 1
            print(max[z], citations[i], counter)

            if counter >= max[z]:
                return max[z]

        return 1  # In case no H-index is found, return 0


# Example usage
sol = Solution()
a = sol.hIndex([11,15])
print(a)



