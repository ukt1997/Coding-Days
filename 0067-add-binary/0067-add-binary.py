class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        ret = ""
        temp = 0
        while a or b or temp:
            if a: temp += int(a.pop())       
            if b: temp += int(b.pop())
            temp, remainder = divmod(temp, 2)
            print(remainder , temp)
            ret = str(remainder) + ret

        return ret   
        