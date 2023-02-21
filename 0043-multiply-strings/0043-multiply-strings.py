class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1[0] == '0' or num2[0] == '0':
            return "0"
        sums_so_far = []
        m = len(num1)
        n = len(num2)
        for i in range(n):
            sum_cur = [0] * i
            mul = int(num2[n-i - 1])
            rem = 0
            for j in range(m):
                cur = int(num1[m-j - 1])
                rem , res = divmod(cur*mul + rem , 10)
                sum_cur.append(res)
            if rem != 0:
                sum_cur.append(rem)
            sums_so_far.append(sum_cur)
        print(sums_so_far)
        ret = ""
        max_digits = len(sums_so_far[-1])
        rem = 0
        for i in range(max_digits):
            res = 0
            for j in range(len(sums_so_far)):
                if len(sums_so_far[j]) > i:
                    res += sums_so_far[j][i]
                    #print(i , res)
            res += rem
            rem , res = divmod(res,10)
            ret = str(res) + ret
        if rem:
            ret = str(rem) + ret
                
                
        return ret
                
                
        