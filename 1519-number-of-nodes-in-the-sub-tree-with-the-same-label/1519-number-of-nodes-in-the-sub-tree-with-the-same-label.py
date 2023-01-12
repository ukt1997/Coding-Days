class Solution:
    def countdfs(self):
        while len(self.stack):
            node = self.stack[-1]
            label = self.labels[node]
            count_index = ord(label) - ord('a')
            if self.ans[node] < 0:
                self.ans[node] = self.count[count_index]
                self.count[count_index] += 1
                
                for child in self.edge_Map[node]:
                    if self.ans[child] < 0:
                        self.stack.append(child)
            else:
                self.stack.pop()
                self.ans[node] = self.count[count_index] - self.ans[node]
                
                
                
                
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        self.edge_Map = defaultdict(list)
        self.ans = [-1]*n
        self.labels = labels
        self.count = [0] * 26
        self.stack = [0]
        for edge in edges :
            self.edge_Map[edge[0]].append(edge[1])
            self.edge_Map[edge[1]].append(edge[0])
        self.countdfs()
        return self.ans
        