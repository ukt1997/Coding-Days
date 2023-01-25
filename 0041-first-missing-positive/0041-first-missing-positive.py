class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        mem = [-1] * (n + 1)
        
        for num in nums:
            if num>= 0 and num<= n:
                mem[num] = 1
        for i in range(1,n+1):
            if mem[i] < 0:
                return i
        return len(nums) + 1
        