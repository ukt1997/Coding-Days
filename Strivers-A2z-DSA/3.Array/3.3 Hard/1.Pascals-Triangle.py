# https://leetcode.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            out = [[1], [1, 1]]
            for i in range(2, numRows):
                # print(i)
                cur = []
                cur.append(1)
                for j in range(len(out[i - 1]) - 1):
                    cur.append(out[i - 1][j] + out[i - 1][j + 1])
                cur.append(1)
                # print(cur)
                out.append(cur)
        return out


