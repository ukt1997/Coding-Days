class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        ret =''
        jump = 2*numRows - 2
        k = 0
        for r in range(0, numRows):
            if(k >= len(s)):
                break
            i = r
            j = r*2
            row_jump = jump - j
            flag = False
            while(i < len(s)):
                if(k >= len(s)):
                    break
                ret += s[i]
                if(r > 0 and r < numRows-1):
                    if(row_jump < jump and row_jump and flag == False):
                        i+=row_jump
                        flag = True
                    elif(row_jump < jump and row_jump and flag):
                        i+=j
                        flag = False
                else:
                    i+=jump
                k+=1
        return ret
        