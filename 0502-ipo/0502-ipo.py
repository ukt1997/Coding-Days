class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = list(zip(capital, profits))
        projects.sort(key = lambda x : -x[0])
        h = []
        for _ in range(k):
            while projects and projects[-1][0] <= w:
                heappush(h, -projects.pop()[1])
            if h:
                w += -heappop(h)
            else:
                break
        
        return w
        