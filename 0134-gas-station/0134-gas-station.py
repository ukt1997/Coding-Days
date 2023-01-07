class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(cost)
        if sum(cost) > sum(gas) :
            return -1
        ret = 0
        cur_gas = 0
        for i in range(n):
            cur_gas += ( gas[i] - cost[i])
            if cur_gas < 0:
                ret = i + 1
                cur_gas = 0
                
        return ret
        