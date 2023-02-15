class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = len(num) - 1
        cur_val = 0
        while k or cur_val :
            k , rem = divmod(k,10)
            #print(k , rem)
            if n>= 0:
                cur_val += num[n]
            cur_val += rem 
            if n >= 0:
                cur_val , num[n] = divmod(cur_val,10)
            else:
                cur_val , temp = divmod(cur_val,10)
                num.insert(0, temp)
            n -= 1
            #print(num)
            
            
        return num
        
        