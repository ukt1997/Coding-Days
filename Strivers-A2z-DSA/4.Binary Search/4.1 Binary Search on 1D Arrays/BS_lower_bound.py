class Solution:
    # User function Template for python3

    # Complete this function
    def findFloor(self, A, N, X):
        # Your code here
        start = 0
        end = N - 1
        while start <= end:
            # print(start,end)
            mid = (start + end) // 2
            if A[mid] == X:
                return mid
            elif X > A[mid]:
                start = mid + 1
            else:
                end = mid - 1
        # print(start,end)
        if start >= N:
            return N - 1
        elif end <= 0:
            return -1
        else:
            return start - 1


# {
# Driver Code Starts
# Initial Template for Python 3


import math


def main():
    T = int(input())
    while (T > 0):
        NX = [int(x) for x in input().strip().split()]
        N = NX[0]
        X = NX[1]

        A = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.findFloor(A, N, X))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends