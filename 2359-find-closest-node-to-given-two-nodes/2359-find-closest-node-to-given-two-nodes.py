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
        n2 = node2
        node2_path[n2] = 0
        cnt = 0
        while edges[n1] != -1 and node1_visited[n1] == -1:
            cnt += 1
            node1_visited[n1] = 1
            if node1_path[edges[n1]] < 0 :node1_path[edges[n1]] = cnt
            n1 = edges[n1]
        cnt = 0
        while edges[n2] != -1 and node2_visited[n2] == -1:
            cnt += 1
            node2_visited[n2] = 1
            if node2_path[edges[n2]] < 0: node2_path[edges[n2]] = cnt
            n2 = edges[n2]
        
        ret = -1
        max_dis = 2*len(edges)
        for i in range(len(edges)):
            p1 = node1_path[i]
            p2 = node2_path[i]
            if p1 >= 0 and p2 >= 0:
                if ret == -1:
                    max_dis = max(p1,p2)
                    ret = i
                elif max_dis > max(p1,p2):
                    max_dis = max(p1,p2)
                    ret = i
            
            
        return ret
        