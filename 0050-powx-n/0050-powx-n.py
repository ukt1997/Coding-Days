class Solution:
    def myPow(self, x: float, n: int) -> float:
        #print("x-n",x,n)
        if n == 0:
            return 1
        ret = 1
        if n < 0:
            n1 = -1*n
        else:
            n1 = n
        
        if(n1%2):
            ret = x * self.myPow(x,n1-1)
        else:
            ret = self.myPow(x*x,n1//2)
        
        if n > 0:
            return ret
        else:
            return 1/ret
            
            
        