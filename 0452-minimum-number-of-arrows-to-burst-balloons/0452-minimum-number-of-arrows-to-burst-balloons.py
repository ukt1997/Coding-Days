class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ret = 1
        # Sorting the Array , Sorting always help in Range Prob.
        points.sort(key = lambda x : x[1])
        print(points)
        refEnd = points[0][1]
        for point in points :
            start,end = point[0],point[1]
            if start > refEnd:
                ret += 1
                refEnd = end
        return ret
        
        