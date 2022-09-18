class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        out = []
        center = 0
        n = len(nums)
        for i in nums:
            if i < 0:
                center += 1
        print(center)
        left = center - 1
        right = center 
        while left >= 0 or right < n:
            if right >= n:
                out.append(nums[left]**2)
                left -= 1
            elif left < 0:
                out.append(nums[right]**2)
                right += 1
            elif (nums[left]**2) > (nums[right]**2):
                out.append(nums[right]**2)
                right += 1
            else:
                out.append(nums[left]**2)
                left -= 1
        return out
        
        