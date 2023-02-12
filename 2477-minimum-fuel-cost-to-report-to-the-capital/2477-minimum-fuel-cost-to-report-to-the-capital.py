class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = collections.defaultdict(list)
        for x, y in roads:
            graph[x].append(y)
            graph[y].append(x)

        visited = set()
        visited.add(0)
        res = 0
        def dfs(root, people):
            nonlocal res
            for node in graph[root]:
                if node not in visited:
                    visited.add(node)
                    people += dfs(node, 1)
            
            if root:
                res += ceil(people/seats)

            return people

        dfs(0, 1)
        return res
        