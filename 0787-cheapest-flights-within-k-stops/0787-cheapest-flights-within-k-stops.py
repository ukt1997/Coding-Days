class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for s, d, p in flights:
            graph[s].append((d, p))

        @cache
        def dfs(node: int, k: int) -> int:
            if k < 0:
                return inf
            if node == dst:
                return 0
            return min((price + dfs(nxt, k-1) for nxt, price in graph[node]), default=inf)
    
        res = dfs(src, k+1)
        return res if res != inf else -1
        