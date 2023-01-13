class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        ret = 0
        childs = defaultdict(list)
        for i, par in enumerate(parent):
            childs[par].append(i)
        print(childs)
        
        def dfs(node):
            # This will Return the Height of Longest path possible via this Node 
            # And Update The ans variable  with maximum path length (checking each node)
            max_l = 0
            max_l2 = 0
            nonlocal ret
            for child in childs[node]:
                temp = dfs(child)
                if s[node] != s[child]:
                    if temp > max_l:
                        # this child path is longest so far
                        max_l2 = max_l
                        max_l = temp
                    elif temp > max_l2:
                        # this child path is 2nd longest so far 
                        # updating only 2nd max path
                        max_l2 = temp
            # Updating Ans (i.e max Path ) to max of all found path so far , or path between 2 childs of this Node 
            ret = max(ret , max_l + max_l2 + 1)
            return max_l + 1
        dfs(0)
        return ret
            
        