class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ret = set()
        for i in range(1,1 << n):
            #print("i =",i)
            cur_seq = []
            for j in range(n):
                #print(i >> j)
                if (i >> j) & 1:
                    cur_seq.append(nums[j])
            #print(cur_seq)
            if len(cur_seq) >= 2 and all(cur_seq[i] <= cur_seq[i+1] for i in range(len(cur_seq) - 1)):
                ret.add(tuple(cur_seq))
                
            
        return ret
        