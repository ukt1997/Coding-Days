class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min_1 = float('inf')
        min_2 = float('inf')
        for num in nums:
            if num <= min_1:
                min_1 = num
            elif num != min_1 and num <= min_2:
                min_2 = num
            else:
                return True
        return False
        