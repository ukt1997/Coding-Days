class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)

        valnode = defaultdict(list)
        for i in range(n):
            valnode[vals[i]].append(i)
        
        valedge = defaultdict(list)
        for i, j in edges:
            valedge[max(vals[i], vals[j])].append((i, j))
        #print(valedge)
        parent = list(range(n))
        def find(k):
            if parent[k] != k:
                parent[k] = find(parent[k])
            return parent[k]
        
        def connect(k1, k2):
            parent[find(k2)] = find(k1)

        res = 0
        for val in sorted(valnode.keys()):
            for i, j in valedge[val]:
                connect(i, j)
                #print(i,j,parent)
            count = defaultdict(int)
            for node in valnode[val]:
                count[find(node)] += 1
            for group in count:
                res += (count[group] * (count[group] + 1))//2
        return res
            
        