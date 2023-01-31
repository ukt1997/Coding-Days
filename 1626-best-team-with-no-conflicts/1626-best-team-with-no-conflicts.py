class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pairs = []
        ret = 0
        for i in range(len(scores)):
            pairs.append([scores[i],ages[i]])
        print(pairs)
        pairs.sort()
        #pairs=[[scores[i],ages[i]] for i in range(0,len(scores))]
        dp=[pairs[i][0] for i in range(len(scores))]
        for i in range(0,len(scores)):
            max_score,max_age=pairs[i]
            for j in range(0,i):
                score,age=pairs[j]
                if(max_age>=age):
                    dp[i]=max(dp[i],max_score+dp[j])
                    #set the condition and add the score accordingly...
        return max(dp)
        