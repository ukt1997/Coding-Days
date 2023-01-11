class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        def dfs(node,parent):
            child_time , total_time = 0,0
            for child in self.edgeList[node]:
                if parent == child:
                    continue
                child_time = dfs(child,node)
                if child_time or hasApple[child]:
                    total_time += (child_time + 2)
            #print(node , total_time)
            return total_time
                
        
        if n <= 1:
            return 0
        else:
            self.edgeList = defaultdict(list)
            for edge in edges:
                self.edgeList[edge[0]].append(edge[1])
                self.edgeList[edge[1]].append(edge[0])
            #print(self.edgeList)
            return dfs(0,-1)
            
        return 0
            