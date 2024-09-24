from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        g = gas
        c = cost
        t = [0] * len(gas)

        for i in range(len(gas)):
            t[i] = g[i] - c[i]  # Calculate gas remaining after cost at each station
            print(f"t[{i}] = {t[i]} after considering gas[{i}] = {g[i]} and cost[{i}] = {c[i]}")
            print(t)

# Example usage
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

s = Solution()
s.canCompleteCircuit(gas, cost)




