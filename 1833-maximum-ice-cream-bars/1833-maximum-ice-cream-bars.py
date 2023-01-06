class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        ret = 0
        costs.sort()
        print(costs)
        for cost in costs:
            if cost > coins:
                break
            else:
                coins -= cost
                ret += 1
        return ret