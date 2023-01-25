class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        if node1 == node2:
            return node1
        node1_path = [-1] * len(edges)
        node1_visited = [-1] * len(edges)
        node2_path = [-1] * len(edges)
        node2_visited = [-1] * len(edges)
        n1 = node1
        node1_path[n1] = 0
        cnt = 0
        while edges[n1] != -1 and node1_visited[n1] == -1:
            #print(n1)
            cnt += 1
            node1_visited[n1] = 1
            if node1_path[edges[n1]] < 0 :node1_path[edges[n1]] = cnt
            n1 = edges[n1]
        n1 = node2
        node2_path[n1] = 0
        cnt = 0
        while edges[n1] != -1 and node2_visited[n1] == -1:
            #print(n1)
            cnt += 1
            node2_visited[n1] = 1
            if node2_path[edges[n1]] < 0: node2_path[edges[n1]] = cnt
            n1 = edges[n1]
        #print(node1_path)
        #print(node2_path)
        
        path = []
        for i in range(len(edges)):
            p1 = node1_path[i]
            p2 = node2_path[i]
            if p1 >= 0 and p2 >= 0:
                path.append((max(p1,p2) , i))
        path.sort()
        #print(path)
            
        return -1 if len(path) == 0 else path[0][1]
        