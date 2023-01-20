class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        ret = 1
        
        #print(pairs)
        max_v = pairs[0][1]
        for i in range(1,len(pairs)):
            if pairs[i][0] > max_v:
                max_v = pairs[i][1]
                ret += 1
            elif pairs[i][1] < max_v:
                max_v = pairs[i][1]
            
            
        return ret 
        