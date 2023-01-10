class Solution:
    def isValid(self, s: str) -> bool:
        self.stack = []
        for ch in s:
            if ch in ('(','{','['):
                self.stack.append(ch)
            elif ch in (')','}',']') and len(self.stack) == 0:
                return False
            elif  self.stack[-1] == '(':
                if ch in ('}',']'):
                    return False
                else:
                    self.stack.pop()
            elif self.stack[-1] == '{':
                if ch in (')',']'):
                    return False
                else:
                    self.stack.pop()
            elif self.stack[-1] == '[':
                if ch in ('}',')'):
                    return False
                else:
                    self.stack.pop()
        if len(self.stack) > 0:
            return False
        return True
                
                    
                
        