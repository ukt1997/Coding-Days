class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def inner_func(start, prev, last_count, K_left):
            if K_left < 0:
                return float("inf") 
            if start >= len(s):
                return 0
            if s[start]==prev:
                incr = 1 if last_count in (1,9,99) else 0 
                return incr + inner_func(start+1, prev, last_count+1, K_left) 
            else:
                keep = 1  + inner_func(start+1, s[start], 1, K_left) 
                delete = inner_func(start+1, prev, last_count, K_left-1) 
                return min(keep, delete)
        return inner_func(0,"", 0,k)
            
            
        
        