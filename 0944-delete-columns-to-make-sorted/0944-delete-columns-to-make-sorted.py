class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs)
        n = len(strs[0])
        
        count = 0
        for col in range(n):
            for row in range(m):
                if row == 0:
                    start = ord(strs[row][col])
                elif ord(strs[row][col]) < start:
                    count += 1
                    break
                else:
                    start = ord(strs[row][col])
        return count
        
        