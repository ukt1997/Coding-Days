class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        first_one = -1
        ret = 0
        for i in range(len(s)):
            if s[i] == '1':
                first_one = i
                break
        if first_one >= 0:
            ones = 0
            zeroes = 0
            for i in range(first_one,len(s)):
                if s[i] == '0':
                    zeroes += 1
                else:
                    ones += 1
                #print(zeroes, ones)
                if ones <= zeroes :
                    ret += ones
                    zeroes = 0
                    ones = 0
            ret += min(zeroes , ones)
            
        return ret
            
            
                
        