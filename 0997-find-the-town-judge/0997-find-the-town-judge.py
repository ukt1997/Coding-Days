class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            if len(trust) == 0:
                return 1
            else:
                return -1
        ret = [0 for i in range(n+1)]
        supporter = []
        for cur in trust:
            ret[cur[1]] += 1
            supporter.append(cur[0])
        #print(ret)
        max_vote = max(ret)
        candidate = [i for i,x in enumerate(ret) if x==max_vote] # => [1, 3]
        #print(candidate)
        if len(candidate) == 1 and max_vote == n - 1 and candidate[0] not in supporter:
            return candidate[0]
        return -1
                
        