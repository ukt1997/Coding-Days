class Solution:
    def can_ship(self , candidate , weights , days):
        current_weight = 0
        days_taken = 1

        for weight in weights:
            current_weight += weight

            if current_weight > candidate :
                days_taken += 1
                current_weight = weight
        return days_taken <= days
        
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l = max(weights)
        r = sum(weights)

        while l < r:
            mid = (l + r)//2
            if self.can_ship(mid,weights,days): r = mid
            else : l = mid + 1
        return r