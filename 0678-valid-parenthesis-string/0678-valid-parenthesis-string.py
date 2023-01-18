class Solution:
    def checkValidString(self, s: str) -> bool:
        # Recursion Solution , But Exceeded Maximum Recursion Length
        # n = len(s)
        # if n == 0:
        #     return True
        # elif n == 1:
        #     if s == "*":
        #         return True
        #     else:
        #         return False
        # elif s == "()":
        #     return True
        # elif s == "*)":
        #     return True
        # elif s == "(*":
        #     return True
        # else:
        #     return self.checkValidString(s[0]+s[n-1]) and self.checkValidString(s[1:-1])
        
        open_max = 0
        open_min = 0
        for ch in s:
            open_min += 1 if ch == "(" else -1
            open_max += 1 if ch != ")" else -1
            if open_max < 0:
                break
            open_min = max(open_min , 0)
        return open_min == 0
            
            
            
            
        