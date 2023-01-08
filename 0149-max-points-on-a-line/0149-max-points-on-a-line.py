class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        result = 0
        
        for i in range(n):
            slope = {}
            for j in range(i+1,n):
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]
                
                cur_slope = ((y2-y1)/(x2-x1)) if x2 != x1 else inf
                
                if cur_slope in slope:
                    slope[cur_slope] += 1
                else:
                    slope[cur_slope] = 2
                    
                result = max(result , slope[cur_slope])                
                    
        return result
                    
        