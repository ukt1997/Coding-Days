class Solution:
    def find_row(self, arr, target):
        m = len(arr)
        n = len(arr[0])

        # find Row
        start = 0
        end = m - 1

        while start <= end:
            mid = (start + end) // 2
            if (arr[mid][0] <= target) and (arr[mid][n - 1] >= target):
                return mid
            elif arr[mid][0] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def find_col(self, arr, row, target):

        n = len(arr[0])

        # find col
        start = 0
        end = n - 1

        while start <= end:
            mid = (start + end) // 2
            if arr[row][mid] == target:
                return mid
            elif arr[row][mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ref_row = self.find_row(matrix, target)
        if ref_row >= 0:
            col = self.find_col(matrix, ref_row, target)
            if col >= 0:
                return True
            else:
                return False

        else:
            return False




