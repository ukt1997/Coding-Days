# https://leetcode.com/problems/set-matrix-zeroes/
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_Row = []
        zero_Col = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_Row.append(i)
                    zero_Col.append(j)
        print(zero_Row, zero_Col)
        for i in set(zero_Row):
            matrix[i] = [0 for i in range(n)]
        for j in range(n):
            if j in set(zero_Col):
                for i in range(m):
                    matrix[i][j] = 0




