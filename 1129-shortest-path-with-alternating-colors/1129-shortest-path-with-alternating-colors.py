class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red=defaultdict(list)
        blue=defaultdict(list)
        for a,b in redEdges:
            red[a].append(b)
        for a,b in blueEdges:
            blue[a].append(b)
        ans=[-1 for i in range(n)]
        q=deque()
        q.append([0,0,None])
        vis=set()
        vis.add((0,None))
        while q:
            node,length,edge_color=q.popleft()
            if ans[node]==-1:
                ans[node]=length
            if edge_color!="RED":
                for i in red[node]:
                    if (i,"RED") not in vis:
                        vis.add((i,"RED"))
                        q.append([i,length+1,"RED"])
            if edge_color!="BLUE":
                for i in blue[node]:
                    if (i,"BLUE") not in vis:
                        vis.add((i,"BLUE"))
                        q.append([i,length+1,"BLUE"])    
        return ans
        