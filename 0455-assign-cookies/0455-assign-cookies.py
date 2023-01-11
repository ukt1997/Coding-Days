class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        print(g)
        print(s)
        i = 0
        ret = 0
        for cg in g:
            while i < len(s) and s[i] < cg:
                i += 1
            print(cg , i)
            if i < len(s) and cg <= s[i]:
                ret += 1
                i += 1
            else:
                break
            
        
        return ret
        