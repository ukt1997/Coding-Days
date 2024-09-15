class Solution:
    
    def helper(self, s , li):
        
        left = li[0]
        right = li[0]
            
        if len(li) == 2:
            right = li[1]
        print(left,right)
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                if right - left + 1 > len(self.ret):
                    self.ret = s[left:right+1]
                left -= 1
                right += 1     
            else:
                break
            
        
    def longestPalindrome(self, s: str) -> str:
        self.ret = ""
        
        for i in range(len(s)):
            self.helper(s,[i])
            self.helper(s,[i,i+1])
        
        return self.ret
        