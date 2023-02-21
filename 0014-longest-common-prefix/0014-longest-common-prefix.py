class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mem = {}
        for cur in strs:
            for i in range(len(cur)):
                if cur[:i+1] in mem.keys():
                    mem[cur[:i+1]] += 1
                else:
                    mem[cur[:i+1]] = 1
        print(mem)
        
        max_str = ''
        max_cnt = len(strs)
        
        for key in mem.keys():
            if mem[key] == (max_cnt)  :
                if len(key) > len(max_str):
                    max_str = key
                    max_cnt = mem[key]
        return max_str
            
        