class Solution:
    def myAtoi(self, s: str) -> int:
        mul = 1
        def get_int(st):
            #print(st)
            if len(st) < 1 or st[0] < '0' or st[0] > '9' :
                #print("Returning 0")
                return 0
            else:
                
                if len(st) >= 2 and st[1] >= '0' and st[1] <= '9':
                    ret =  get_int(st[1:]) + ( (ord(st[0]) - ord('0')) * self.mul )
                else:
                    ret = ( (ord(st[0]) - ord('0')))
                self.mul = self.mul*10
                #print("Returning ",ret)
                #print("Multiplier ",self.mul)
                return ret
        if s:
            n = len(s)
            self.mul = 1
            pos = 1
            i = 0
            while s[i] == ' ':
                i += 1
                if i>=n:
                    return 0
            if i < n and s[i] == '-':
                pos = -1
                i+= 1
            elif i < n and s[i] == '+':
                i += 1
            if len(s[i:])>0 and s[i] >= '0' and s[i] <= '9':
                val=  get_int(s[i:])
                if pos > 0:
                    return min(val,2147483647)
                else:
                    return max(-1*val,-2147483648)
            else:
                return 0
        else:
            return 0
        
            
        