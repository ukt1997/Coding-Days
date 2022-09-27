# https://practice.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=leaders-in-an-array
class Solution:
    # Back-end complete function Template for Python 3

    # Function to find the leaders in the array.
    def leaders(self, A, N):
        # Code here
        leaders = [A[N - 1]]  # Last Element
        cnt = 0
        for i in reversed(range(N - 1)):
            if A[i] >= leaders[cnt]:
                leaders.append(A[i])
                cnt += 1
        return reversed(leaders)


# {
# Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        obj = Solution()

        A = obj.leaders(A, N)

        for i in A:
            print(i, end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends