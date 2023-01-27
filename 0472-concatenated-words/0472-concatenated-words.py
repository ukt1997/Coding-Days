class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        memory = set(words)
        ret = []
        for word in words:
            #print(word)
            length = len(word)
            dp = [False] * (length + 1)
            dp[0] = True
            
            for i in range(1, length+1):
                for j in range((i == length) and 1 or 0, i):
                    #print(j,i)
                    if not dp[i]:
                        dp[i] = dp[j] and word[j:i] in memory
                        #print("Found ",word[:i])
            if dp[length]:
                ret.append(word)
                #print(ret)
                      
        return ret
        