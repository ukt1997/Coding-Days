class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        ret = n-1
        min_jump = [i for i in range(n)]
        #print(min_jump)
        for i in range(n):
            for j in range(i+1 , min(n,i+nums[i]+1)):
                min_jump[j] = min(min_jump[j] , min_jump[i] + 1)
                if j == n-1:
                    ret = min(ret ,min_jump[j] )
        #print(min_jump)
        
                
        return ret