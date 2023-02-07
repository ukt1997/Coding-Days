class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        l, r, ans = 0, 0, 0
        while r < len(fruits):
            if fruits[r] in basket:
                basket[fruits[r]] += 1
            else:
                basket[fruits[r]] = 1
            
            #Adjusting the window so that the subarray will contain at most 2 distinct integer
            while len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                l += 1
            
            #Updating the ans
            ans = max(ans, (r-l)+1)
            r += 1     
        
        return ans
        