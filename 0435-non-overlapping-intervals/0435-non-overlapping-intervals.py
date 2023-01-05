class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ret = 0
        # Sorting the Array , Sorting always help in Range Prob.
        intervals.sort(key = lambda x : x[1])
        print(intervals)
        refEnd = float('-inf')
        for point in intervals:
            start,end = point[0],point[1]
            if start >= refEnd:
                # Means Cur Pair is not overlapping with previous pairs 
                # So increase End
                refEnd = end
            else:
                # Means this one overlapping with last and may be other previously processed pairs 
                # So remove it 
                ret += 1
                
        return ret