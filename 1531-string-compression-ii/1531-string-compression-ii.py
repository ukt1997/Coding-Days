class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def inner_func(start, prev, last_count, K_left):
            if K_left < 0:
                # terminating conditin when K is over 
                return float("inf") 
            if start >= len(s):
                # terminating conditin when Start pointer passed whole string 
                return 0
            if s[start]==prev:
                # will add cur char to the string , We are not trying skipping it here as this we have already tried while selecting the 1st occurance of this char , No point in adding 1st a out of aaa and skipiing any of 2nd or 3rd in all these scenarios resultent will be aa only . 
                incr = 1 if last_count in (1,9,99) else 0 
                return incr + inner_func(start+1, prev, last_count+1, K_left) 
            else:
                # will check if we need to keep this char or skip this and go with min of that 
                keep = 1  + inner_func(start+1, s[start], 1, K_left) 
                delete = inner_func(start+1, prev, last_count, K_left-1) 
                return min(keep, delete)
        return inner_func(0,"", 0,k)
            
            
        
        