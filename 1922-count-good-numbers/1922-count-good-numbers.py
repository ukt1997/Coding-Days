class Solution:
    MOD = 1000000007
    #(4 * 5) ^ (n / 2); if odd, (4 * 5) ^ (n / 2) * 5.
    def power(self, m , n):
        if n == 0:
            return 1
        ret = self.power(m,n//2) % self.MOD
        if n%2 == 0:
            return (ret*ret)%self.MOD
        else:
            return (((ret*ret)%self.MOD)*m) % self.MOD
        
    def countGoodNumbers(self, n: int) -> int:
        even_digits = [0,2,4,6,8]
        prime_digits = [2,3,5,7]
        
        ret = self.power((4*5),n//2)%self.MOD
        if n%2 != 0:
            return (5*ret) % self.MOD
        else:
            return ret
            
            
        