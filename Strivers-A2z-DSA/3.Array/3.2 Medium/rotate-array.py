# https://leetcode.com/problems/rotate-image/
class Solution:
    def print_array(self, matrix):
        for row in matrix:
            print(row)

    def Transpose(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(rows):
            for col in range(row, cols):
                # print(row,col)
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp
        # self.print_array(matrix)

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.Transpose(matrix)
        cols = len(matrix[0])
        for row in matrix:
            for j in range(cols // 2):
                tmp = row[j]
                row[j] = row[cols - j - 1]
                row[cols - j - 1] = tmp

