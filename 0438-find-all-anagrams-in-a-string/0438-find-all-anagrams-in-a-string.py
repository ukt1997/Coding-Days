class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        Match = [0] * 26     
        for i in range(len(p)):
            Match[ord(p[i]) - 97] += 1  
        
        check = [0] * 26
        left, right = 0,0
        ret = []
        
        while right < len(s):
            check[ord(s[right]) - 97] += 1
            if check == Match:
                ret.append(left)
            if right - left + 1 == len(p):
                check[ord(s[left]) - 97] -= 1
                left += 1
            right += 1
        return ret
        