class Solution:
    def beautySum(self, s: str) -> int:
        total = 0
        n = len(s)
        for i in range(n - 2):
            dic = {}
            for j in range(i, n):
                # print(s[i:j+1])
                dic.setdefault(s[j], 0)
                dic[s[j]] += 1
                # print(dic)
                total += (max(dic.values()) - min(dic.values()))
                # print(total)
        return total

