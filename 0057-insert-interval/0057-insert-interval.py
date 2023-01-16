class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def merge1(interval , index):
            start = interval[index][0]
            end = interval[index][1]
            while index > 0:
                prev = interval[index - 1]
                if start <= prev[1]:
                    end = max(end ,prev[1])
                    interval.pop(index)
                    index -= 1
                    start = min(start,prev[0])
                else:
                    break
            interval[index] = [start,end]
            return index
                           
        def merge2(interval,index):
            start = interval[index][0]
            end = interval[index][1]
            while index < len(interval) - 1:
                nxt = interval[index + 1]
                print(nxt)
                if end >= nxt[0]:
                    interval.pop(index)
                    end = max(end,nxt[1])
                else:
                    break
            interval[index] = [start,end]
            return index
        intervals.append(newInterval)
        intervals.sort()
        i = intervals.index(newInterval)
        print(i , intervals)
        i = merge1(intervals,i)
        print(i , intervals)
        i = merge2(intervals,i)
        return intervals
        