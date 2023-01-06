class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        start = 0
        end = n - 1
        vol = 0
        while start < end :
            cur_vol = min(height[start],height[end]) * (end - start)
            if cur_vol > vol:
                vol = cur_vol
            
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        print(vol)
        return vol
            
            
        